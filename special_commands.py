import os
import time
from bot import bot
from PostgreSQL import PostgreSQL
import config


@bot.message_handler(commands=['create'])
def find_file_ids(message):
    db=PostgreSQL(config.database_name)
    db.delete_all("music")
    for file in os.listdir('music'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)

@bot.message_handler(commands=['add'])
def add_music_to_db(message):
    db = PostgreSQL(config.database_name)
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