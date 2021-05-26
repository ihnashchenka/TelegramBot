import logging
import random


class Song:
    # id
    # file_id
    # name

    def __init__(self, m_id, db):
        self.__id = m_id
        self.__file_id = None
        self.__name = None
        song = None
        try:
            song = db.exec_select("""SELECT * FROM music WHERE "M_ID"='%s';""", (self.__id,))[0]
            # format [(4, 'AwADAgADRQMAAoFAiUmLYiTyfoFvtwI', 'J-Five - Fing a way')]
            logging.debug("selectSong=" + str(song))
        except:
            logging.error("Request to db failed when select a song!", exc_info=True)
        if not song or len(song) < 3:
            logging.error("Song wasn't extracted!(Song.__init__)")
        self.__file_id = song[1]
        self.__name = song[2]

    def getFileId(self):
        return self.__file_id

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id

    # get 'count' number of songs names from the database(table 'music')
    # with the exclude of song with ID equal to  'ignore'
    @staticmethod
    def getRandomNames(count, ignore, db):
        names = []
        logging.info("Generating random song names...")
        max = db.count_rows('music');
        ids = random.sample([x for x in range(1, max) if x != ignore], count)
        logging.debug("Songs ids generated:" + str(ids))
        for id in ids:
            # format [("Bon Jovi - It's my life",)]
            new_name = db.exec_select("""SELECT "NAME" FROM music WHERE "M_ID"=%s;""", (id,))[0][0]
            logging.debug("New name selected=" + str(new_name))
            logging.debug("New name type=" + str(type(new_name)))
            names.append(new_name)
        logging.debug("Generated set of name=" + str(names))
        return names
