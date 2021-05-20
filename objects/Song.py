import logging
from utils.PostgreSQL import PostgreSQL
class Song:
    #id
    #file_id
    #name

    def __init__(self,id,db):
        self.__id = id
        self.__file_id=None
        self.__name=None
        try:
            song = db.exec_select("""SELECT * FROM music WHERE "M_ID"='%s';""", (self.__id,))[0]
            # format [(4, 'AwADAgADRQMAAoFAiUmLYiTyfoFvtwI', 'J-Five - Fing a way')]
            logging.debug("selectSong=" + str(song))
        except Exception as e:
            logging.error("Request to db failed when select a song!", exc_info=True)
            return None
        if not song or len(song) < 3:
            logging.error("Song wasn't extracted!(Song.__init__)")
            return None
        self.__file_id = song[1]
        self.__name = song[2]


    def getFileId(self):
        return self.__file_id

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id
