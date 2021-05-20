from utils.PostgreSQL import PostgreSQL
import config
import random
import logging

#get 'count' number of songs names from the database(table 'music')
#with the exclude of song with ID equal to  'ignore'
def getRandomNames(count,ignore):
    names = []
    for i in range(0,count):
        logging.info()
        db = PostgreSQL(config.database_name)
        id = random.randint(1, db.count_rows('music'))
        if id == ignore:
            i -= 1
            continue
        else:
            new_name = db.exec_select("SELECT NAME FROM music WHERE ID=" + id + ";")
            names.append(new_name)
    return names

