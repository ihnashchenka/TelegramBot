import config
import telebot
from random import shuffle
from Game import Game
import utils
from PostgreSQL import PostgreSQL
import os
from flask import Flask, request
import time


bot = telebot.TeleBot(config.token)
server = Flask(__name__)

@bot.message_handler(commands=['game'])
def play(message):
    print("ongame")
    new_game = Game(message.from_user.id)
    bot.send_message(message.chat.id, 'User ' + message.from_user.first_name + ' has started the game')
    bot.send_voice(message.chat.id, new_game.get_song())
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True,selective=True)
    options = new_game.get_answers()
    shuffle(options)
    for item in options:
        markup.row(item)
    bot.reply_to(message, text=message.from_user.first_name + " please, choose the option",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def answer_to_all(message):
    if utils.is_in_game(message.from_user.id):
        cur_game = Game(message.from_user.id)
        if message.text == cur_game.get_right_answer():
            bot.send_message(message.chat.id, text=message.from_user.first_name + ", you are right!!!")
            #some other way to hide keyboard
            #bot.reply_to(message, text=message.from_user.first_name + ", you are right!!!",
                   #      reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        else:
            bot.send_message(message.chat.id, text=message.from_user.first_name + ",sorry, you are wrong(((")
           #bot.reply_to(message, text=message.from_user.first_name + ",sorry, you are wrong(((",
                   #      reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        cur_game.finish()
    else:
        bot.send_message(message.chat.id, "hi")

@server.route("/572372007:AAGM0l1TxBwuT3RR6WIClR3uOyl47ntSKl8", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    print('start')
    bot.remove_webhook()
    bot.set_webhook(url="https://fathomless-thicket-27571.herokuapp.com/572372007:AAGM0l1TxBwuT3RR6WIClR3uOyl47ntSKl8")
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 54321))

'''
if __name__ == '__main__':
    state = "ckeck"
    db = PostgreSQL(config.database_name)
    print(db.select_all("music"))
    print(db.select_all("users"))
    bot.polling(none_stop=True)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
'''