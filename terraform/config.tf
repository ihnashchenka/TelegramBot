variable "app_name" {
  description = "Name of the Heroku app provisioned for TeleBot"
  default     = "guessmu-3-telebot"
}

variable "default_telebot_buildpack" {

default = "https://github.com/heroku/heroku-buildpack-python.git"
}

variable "source_code_repo" {
default = "ihnashchenka/TelegramBot"
}

variable "source_code_archive_url" {
default  = "https://github.com/ihnashchenka/TelegramBot/tarball/master"
}