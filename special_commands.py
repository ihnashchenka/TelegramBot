# Is not a part of a bot.
# Technical use only to import set of audio file to Telegram and bot's db

# to use command /create:
# copy methods find_file_ids() and add_music_to_db() to bot.py ABOVE answer_to_all()
# check that all import statements from this file exists in bot.py
# put all file you are uploading to music/ folder (do not include it to git repo)
# run the bot

# DO NOT PUSH  BOT.PY WITH /CREATE COMMAND
# IT MUST ALWAYS BE IN SPECIAL_COMMANDS.PY

import os
import time
from bot import bot
from utils.PostgreSQL import PostgreSQL
import config
import logging

@bot.message_handler(commands=['create'])
def find_file_ids(message):
    db = PostgreSQL(database_name)
    for file in os.listdir('music'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            add_music_to_db(db, msg.voice.file_id, file.split('.')[0])
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)
    db.close()


def add_music_to_db(db, file_id, name):
    try:
        db.exec_update("""INSERT INTO music("M_ID","FILE_ID", "NAME") VALUES(nextval('music_seq'),%s,%s);""", (file_id, name,))
        logging.info("Song added: " + str(file_id) + " name: " + str(name))
    except:
        logging.error("Can't insert song: " + str(file_id) + " name: " + str(name),exc_info=True)



    '''
    db.add("music","1,AwADAgADQgMAAoFAiUmmd8BB8bzTJgI, The Police - Every breth you take,"
                   "'Ellie Goulding - Love me you do,Fall Out Boys - Immortals,J-Five - Fing a way'")
    db.add("music", "2,AwADAgADQwMAAoFAiUlwCWqVa0bduQI,Coolio - Ganstas paradise,"
                    "'J-Five - Fing a way, The Police - Every breth you take, The Eagles - Hotel California'")
    db.add("music", "3,AwADAgADRAMAAoFAiUm41RPJX8qrlwI,Bon Jovi - It's my life,"
                    "'Coolio - Ganstas paradise, Darre Hayse - Insatiable,Ellie Goulding - Love me you do'")
    db.add("music", "4,AwADAgADRQMAAoFAiUmLYiTyfoFvtwI,J-Five - Fing a way,"
                    "'Darre Hayse - Insatiable,The Police - Every breth you take,Ellie Goulding - Love me you do'")
    db.add("music", "5,AwADAgADRgMAAoFAiUmjiOSWEbj02AI,Ellie Goulding - Love me you do,"
                    "'Bon Jovi - It's my life,Coolio - Ganstas paradise,Darre Hayse - Insatiable'")
    db.add("music", "6,AwADAgADRwMAAoFAiUkVHJbwu21GEAI,The Eagles - Hotel California,"
                    "'Coolio - Ganstas paradise, Darre Hayse - Insatiable,Ellie Goulding - Love me you do'")
    db.add("music", "7,AwADAgADSAMAAoFAiUlD8kfwCs9ibQI, Darre Hayse - Insatiable,"
                    "'Coolio - Ganstas paradise, The Eagles - Hotel California,Ellie Goulding - Love me you do'")
    db.add("music", "8,AwADAgADSQMAAoFAiUml3s0eBdL4wAI, Fall Out Boys - Immortals,"
                    "'Coolio - Ganstas paradise, The Eagles - Hotel California,Ellie Goulding - Love me you do'")
    '''
