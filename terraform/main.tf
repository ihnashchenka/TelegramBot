terraform {
  required_providers {
    heroku = {
      source  = "heroku/heroku"
      version = "4.8.0"
    }
    herokux = {
      source  = "davidji99/herokux"
      version = "0.33.1"
    }
  }
}

provider "herokux" {
  api_key = var.heroku_api_key
}

provider "heroku" {
  email   = var.heroku_email
  api_key = var.heroku_api_key
}



resource "heroku_app" "telebot" {
  name   = var.app_name
  region = "us"

}

resource "heroku_build" "telebot_build" {
  app        = heroku_app.telebot.name
  buildpacks = [var.default_telebot_buildpack]
  
  source {
    url = var.source_code_archive_url
  }
}

resource "heroku_formation" "bot_instance" {
  app        = heroku_app.telebot.id
  type       = "web"
  quantity   = 1
  size       = "Free"
  depends_on = [heroku_build.telebot_build]
}

locals {
    webhook_url = join("",["https://", heroku_app.telebot.name, ".herokuapp.com/", var.telegram_token])

}
resource "heroku_config" "env" {
  sensitive_vars = {
    TELEGRAM_TOKEN = var.telegram_token
   # WEBHOOK_URL    = "https://${heroku_app.telebot.name}.herokuapp.com/${var.telegram_token}"
    WEBHOOK_URL    = local.webhook_url
  }
}

resource "heroku_app_config_association" "config" {
  app_id         = heroku_app.telebot.id
  sensitive_vars = heroku_config.env.sensitive_vars
}


resource "heroku_app_webhook" "telebot_webhook" {
  app_id  = heroku_app.telebot.id
  level   = "notify"
//  url     = "https://${heroku_app.telebot.name}.herokuapp.com/${var.telegram_token}"
    url = local.webhook_url
  include = ["api:release"]
}

resource "heroku_pipeline" "deployment" {
  name = "deployment-pipeline"
}


resource "heroku_pipeline_coupling" "prod" {
  app      = heroku_app.telebot.id
  pipeline = heroku_pipeline.deployment.id
  stage    = "production"
}


resource "herokux_pipeline_github_integration" "github" {
  pipeline_id = heroku_pipeline.deployment.id
  org_repo    = var.source_code_repo
}

resource "heroku_addon" "database" {
    app = heroku_app.telebot.name
   # name = "telebot-data"
    plan =  "heroku-postgresql:hobby-dev"
}

output "heroku_addon_data_basic" {
  value = [
    "Created database",
    "id: ${heroku_addon.database.id}",
    "name: ${heroku_addon.database.name}",
    "app: ${heroku_addon.database.app}",
    "plan: ${heroku_addon.database.plan}",
    "config_vars: ${join(", ", heroku_addon.database.config_vars)}",
  ]
}
