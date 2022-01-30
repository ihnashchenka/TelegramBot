#database_name='d9bsan98ui4ua8'

# messages
hello_msg = "Hi! I am GuessMu 3.0 bot. I am here to play 'Guess the Melody' game with you." \
            "Send /game to me to start. Use /help command to see more options."

list_of_commands = "Here is commands know: \n /hello - just a few words about me;" \
                   "\n/game - choose to start or continue a game;" \
                   "\n/end_game - terminate ongoing game;" \
                   "\n/hide - hide keyboard with answers if you have one;" \
                   "\n/delete_me - delete all information about your user from the bot database: "\
                   "game statistics, active game and the fact that you have ever interact with a bot;"\
                   "\n/help - list of commands I understand;"

default_msg = "I don't know yet what does it mean. Please use /help to see available commands."

game_stopped = "Your game was stopped. Start a new one using /game command."

no_game_to_stop = "Looks like you have no active game... You can start one using /game command."

internalError = "Something went wrong. Please, try again."

user_deleted = "All information about you was deleted from my database: active games, game statistic." \
               "Now you are a total stranger to me. Who are you?" \
               "If you would like to start it over just send me /hello or /game ."

already_deleted = "I don't have you in the my database."
