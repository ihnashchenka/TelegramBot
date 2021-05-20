from utils.PostgreSQL import PostgreSQL
import config
import random
import logging
from utils import music
from objects.Song import Song
from objects.User import User
import json


class Game:
    # user
    # id
    # song
    # answers

    NUMBER_OF_ANSWERS = 4

    def save(self, db):
        try:
            db.exec_insert("""INSERT INTO games("USER_ID","MUSIC_ID","ANSWERS") VALUES(%s, %s, %s)""", (self.__user.getId(), self.__song.getId(), self.__answers,))
        except:
            logging.error("Can't save a game!",exc_info=True)
            return False
        logging.info("Game saved.")

        return True

    # unit test 1 - send a user id that has no game. Result = None
    # unit test 2 - send a user which has a game(preliminary insert it). Result = all fields are set
    # unit test 3 - connection failed(db=null) Result = None

    def getGame(self, user, db):
        self.__user = user
        try:
            game = db.exec_select("""SELECT "G_ID", "MUSIC_ID", "ANSWERS" FROM games WHERE "USER_ID"=%s""",
                                  (self.__user.getId(),))[0]
            #format [(.,.,.)]
            # todo what if more than one game found for a user?
        except Exception as e:
            logging.error("Request to db failed when extracting a game!", exc_info=True)
            return None
        if not game or len(game) < 3:
            logging.error("Game wasn't extracted from db! (Game.getGame)")
            logging.debug("game=" + str(game))
            return None
        self.__id = game[0]
        self.__song = Song(game[1],db)
        self.__answers = game[2]
        return self

#true if successfully saved
    def startGame(self, user, db):
        logging.info("Starting a new game...")
        self.__user = user
        song_id = random.randint(1, db.count_rows('music'))
        self.__song = Song(song_id, db)
        if not self.__song:
            return None
        #todo do not do intermidiete copies on __answers
        wrong_answers =music.getRandomNames(self.NUMBER_OF_ANSWERS - 1, self.__song.getId(),db)
        wrong_answers.append(self.__song.getName())
        self.__answers = wrong_answers
        logging.debug("Answers generated for a new game:")
        logging.debug("answers=" + str(self.__answers))
        self.save(db)


    def __init__(self, user, db):
        self.__user = None
        self.__id = None
        self.__song = None
        self.__answers = None
        if user.isInGame(db):
            self.getGame(user, db)
        else:
            self.startGame(user, db)

    def get_answers(self):
        return self.__answers

    def get_song_file_id(self):
        return self.__song.getFileId()

    def get_right_answer(self):
        return self.__song.getName()

    def finish(self,db):
        try:
            db.exec_insert("""DELETE FROM games WHERE "G_ID"=%s;""",(self.__id,))
            return True
        except:
            logging.error("Can't finish the game!",exc_info=True)
            return False
