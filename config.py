token = '1897318386:AAFkGWrGdZZaBYAAc0Ih0TpERyPjRcwz9SY'
# token = '572372007:AAGM0l1TxBwuT3RR6WIClR3uOyl47ntSKl8'

database_name = 'd9bsan98ui4ua8'

# previous db
# postgre_conn_string = "host='tantor.db.elephantsql.com' dbname='tsbgxbxm' user='tsbgxbxm' password='w0tmJEUr3lqERPmYnt5kDmEqUnilJRWL'"

postgre_conn_string = "host='ec2-54-90-13-87.compute-1.amazonaws.com' dbname='d9bsan98ui4ua8' user='nizfpspbzckvgk' password='a1c6d8aea3bb12bf2b1aefefc5e59d3798f25676b1db2faf8134102eba4bde5d'"

webhook_url = "https://fathomless-thicket-27571.herokuapp.com/572372007:AAGM0l1TxBwuT3RR6WIClR3uOyl47ntSKl8"

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
