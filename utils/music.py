from utils.PostgreSQL import PostgreSQL
import config
import random
import logging

#get 'count' number of songs names from the database(table 'music')
#with the exclude of song with ID equal to  'ignore'
def getRandomNames(count,ignore, db):
    names = []
    logging.info("Generating random song names...")
    max = db.count_rows('music');
    ids = random.sample([x for x in range(1,max) if x != ignore], count)
    print("ids generated:")
    print(ids)
    for id in ids:
        new_name = db.exec_select("""SELECT "NAME" FROM music WHERE "M_ID"=%s;""",(id,))[0][0]
        print(type(new_name))
        #format [("Bon Jovi - It's my life",)]
        names.append(new_name)
    print("Generated answers:")
    print(names)
    return names

def getSongFileID(song_id):
    db = PostgreSQL(config.database_name)
    file_id = db.exec_select("""SELECT "FILE_ID" FROM music WHERE "ID"=%s;""", (song_id,))[0]
    return file_id
