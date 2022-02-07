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

resource "heroku_formation" "telebot" {
  app        = heroku_app.telebot.id
  type       = "web"
  quantity   = 1
  size       = "Free"
  depends_on = [heroku_build.telebot_build]
}

locals {
  webhook_url = join("", ["https://", heroku_app.telebot.name, ".herokuapp.com/", var.telegram_token])
}

resource "heroku_config" "telebot_config" {
  sensitive_vars = {
    TELEGRAM_TOKEN = var.telegram_token
    WEBHOOK_URL    = local.webhook_url
  }
}

resource "heroku_app_webhook" "telebot_webhook" {
  app_id  = heroku_app.telebot.id
  level   = "notify"
  url     = local.webhook_url
  include = ["api:release"]
}

resource "heroku_pipeline" "telebot" {
  name = "deployment-pipeline"
}

resource "heroku_pipeline_coupling" "telebot_prod" {
  app      = heroku_app.telebot.id
  pipeline = heroku_pipeline.telebot.id
  stage    = "production"
}

resource "herokux_pipeline_github_integration" "telebot_github" {
  pipeline_id = heroku_pipeline.telebot.id
  org_repo    = var.source_code_repo
}

resource "heroku_addon" "database" {
  app  = heroku_app.telebot.name
  plan = "heroku-postgresql:hobby-dev"
  provisioner "local-exec" {
    command = "heroku pg:backups:restore ${var.db_initial_load_dump} DATABASE_URL --app ${heroku_app.telebot.name} --confirm ${heroku_app.telebot.name}"
  }
}

output "heroku_addon_data_basic" {
  value = [
    "Created application",
    "id: ${heroku_app.telebot.id}",
    "name: ${heroku_app.telebot.name}",
    "Created pipeline",
    "id: ${heroku_pipeline.telebot.id}",
    "id: ${heroku_pipeline.telebot.name}",
    "Created database",
    "id: ${heroku_addon.database.id}",
    "name: ${heroku_addon.database.name}",
    "app: ${heroku_addon.database.app}",
    "config_vars: ${join(", ", heroku_addon.database.config_vars)}",
  ]
}
