import config
import telebot
import logging
from random import shuffle
from Game import Game
import utils
import os
from flask import Flask, request
import sys


bot = telebot.TeleBot(config.token)
server = Flask(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO,  format='%(levelname)s - %(message)s')

@bot.message_handler(commands=['hello'])
def help(message):
    logging.info('Saying hi!')
    bot.send_message(message.chat.id, config.hello_msg)


@bot.message_handler(commands=['game'])
def play(message):
    logging.info('Starting a game')
    new_game = Game(message.from_user.id)
    bot.send_message(message.chat.id, 'User ' + message.from_user.first_name + ' has started the game')
    bot.send_voice(message.chat.id, new_game.get_song())
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,selective=True)
    options = new_game.get_answers()
    shuffle(options)
    for item in options:
        markup.row(item)
    bot.reply_to(message, text=message.from_user.first_name + " please, choose the option",
                     reply_markup=markup)

@bot.message_handler(commands=['end_game'])
def end_game(message):
    logging.info('Finishing a game')
    if Game.hasGame(message.from_user.id):
        curr_game = Game(message.from_user.id)
        curr_game.finish()
        bot.send_message(message.chat.id, text=config.game_stopped,
                 reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
    else:
        bot.send_message(message.chat.id, text=config.no_game_to_stop)

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
    if utils.is_in_game(message.from_user.id):
        cur_game = Game(message.from_user.id)
        if message.text == cur_game.get_right_answer():
            bot.send_message(message.chat.id, text=message.from_user.first_name + ", you are right!!!",
                             reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        else:
            bot.send_message(message.chat.id, text=message.from_user.first_name + ",sorry, you are wrong(((",
                             reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        cur_game.finish()
    else:
        logging.info('Text received from a user without active game')
        bot.send_message(message.chat.id, config.default_msg)

@server.route('/'+config.token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

'''
if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=config.webhook_url)
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 8443))
    logging.info('GuessMu 3.0 bot started')
'''

if __name__ == '__main__':
    bot.remove_webhook()
    logging.info('GuessMu 3.0 bot started in polling state')
    bot.polling(none_stop=True)


'''
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    
    
if __name__ == '__main__':
     bot.polling(none_stop=True)
'''