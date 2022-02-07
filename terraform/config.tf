variable "app_name" {
  description = "Name of the Heroku app provisioned for TeleBot"
  default     = "guessmu-3-telebot"
}

variable "dbname" {
  description = "Name of the Heroku app provisioned for TeleBot"
  default     = "guessmu-3-database"
}

variable "default_telebot_buildpack" {

  default = "https://github.com/heroku/heroku-buildpack-python.git"
}

variable "source_code_repo" {
  default = "ihnashchenka/TelegramBot"
}

variable "source_code_archive_url" {
  default = "https://github.com/ihnashchenka/TelegramBot/tarball/master"
}

variable "db_initial_load_dump" {
  default = "https://github.com/ihnashchenka/TelegramBot/raw/57cca69823634ec29e6e46b9392b987fbef8842e/db/initial_load.dump"
}