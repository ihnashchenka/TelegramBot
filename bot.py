import config
import telebot
import logging
import sys
import os
from flask import Flask, request
from objects.Game import Game
from objects.User import User
from utils.PostgreSQL import PostgreSQL
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TELEGRAM_TOKEN', '')
webhook_url = "https://fathomless-thicket-27571.herokuapp.com/" + token

bot = telebot.TeleBot(token)
server = Flask(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(levelname)s - %(message)s')


def prepareMarkupKeybord(game):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    options = game.get_answers()
    for item in options:
        markup.row(item)
    return markup


@bot.message_handler(commands=['hello'])
def hello(message):
    logging.info('Saying hi!')
    bot.send_message(message.chat.id, config.hello_msg)

@bot.message_handler(commands=['game'])
def play(message):
    try:
        logging.info('Game command received')
        db = PostgreSQL()
        new_game = Game(User(message.from_user.id, db), db)
        bot.send_message(message.chat.id, 'User ' + message.from_user.first_name + ' has started the game')
        bot.send_voice(message.chat.id, new_game.get_song_file_id())
        bot.reply_to(message, text=message.from_user.first_name + " please, choose the option",
                     reply_markup=prepareMarkupKeybord(new_game))
        db.close()
    except:
        bot.send_message(message.chat.id, text=config.internalError,
                         reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        logging.error("Command /game failed with internalError: ", exc_info=True)



@bot.message_handler(commands=['end_game'])
def end_game(message):
    try:
        logging.info('Finishing a game')
        db = PostgreSQL()
        user = User(message.from_user.id, db)
        if user.isInGame(db):
            curr_game = Game(user, db)
            curr_game.finish(db)
            bot.send_message(message.chat.id, text=config.game_stopped,
                         reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        else:
            bot.send_message(message.chat.id, text=config.no_game_to_stop)
        db.close()
    except:
        bot.send_message(message.chat.id, text=config.internalError,
                         reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        logging.error("Command /end_game failed with internalError: ", exc_info=True)

@bot.message_handler(commands=['delete_me'])
def delete_user(message):
        try:
            logging.info('Deleting a user')
            db = PostgreSQL()
            if not User.exists(message.chat.id,db):
                bot.send_message(message.chat.id, text=config.already_deleted)
                return True
            user = User(message.from_user.id, db)
            if user.delete(db):
                bot.send_message(message.chat.id, text=config.user_deleted,
                                 reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
            db.close()
        except:
            bot.send_message(message.chat.id, text=config.internalError,
                             reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
            logging.error("Command /delete_me failed with internalError: ", exc_info=True)



@bot.message_handler(commands=['help'])
def help(message):
    logging.info('Providing help')
    bot.send_message(message.chat.id, config.list_of_commands)


@bot.message_handler(commands=['hide'])
def hide_answers(message):
    logging.info('Hiding a keyboard')
    bot.send_message(message.chat.id, text='Removing the keyboard...',
                     reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))

@bot.message_handler(func=lambda message: True, content_types=['text'])
def answer_to_all(message):
    db = PostgreSQL()
    user = User(message.from_user.id, db)
    if user.isNew():
        hello(message)
        return
    if user.isInGame(db):
        cur_game = Game(user, db)
        if message.text == cur_game.get_right_answer():
            bot.send_message(message.chat.id, text=message.from_user.first_name + ", you are right!!!",
                             reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
            user.addWin(db)
        else:
            bot.send_message(message.chat.id, text=message.from_user.first_name + ",sorry, you are wrong(((",
                             reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
            user.addGame(db)
        cur_game.finish(db)
    else:
        logging.info('Text received from a user without active game')
        bot.send_message(message.chat.id, config.default_msg)
    db.close()



@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


if __name__ == '__main__':
    try:
        bot.remove_webhook()
        bot.set_webhook(url=webhook_url)
        server.run(host="0.0.0.0", port=os.environ.get('PORT', 8443))
        logging.info('GuessMu 3.0 bot started')
    except:
        logging.fatal("Exception in __main__ !",exc_info=True)

'''
###local debug function
if __name__ == '__main__':
    try:
        bot.remove_webhook()
        logging.info('GuessMu 3.0 bot started in polling state')
        bot.polling(none_stop=True)
    except:
        logging.fatal("Exception in __main__ !",exc_info=True)

'''