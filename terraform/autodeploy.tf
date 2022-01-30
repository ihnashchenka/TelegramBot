/* resource "herokux_app_github_integration" "autodeploy" {
  app_id = heroku_app.telebot.uuid
  branch = "master"
  auto_deploy = true
  depends_on = [herokux_pipeline_github_integration.github, heroku_app.telebot]
} */