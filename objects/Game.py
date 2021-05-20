from PostgreSQL import PostgreSQL
import config
import random
import logging

class Game:
    def __init__(self, user):
        self.user_id = user.id
        db = PostgreSQL(config.database_name)
        game = db.exec_select("SELECT * FROM games WHERE USER_ID="+self.user_id + ";")

        if not game:
            logging.info('User doesn\'t have active games')

            song_id = random.randint(1, db.count_rows('music'))
            song = db.select_single('music', song_id)
            item = list(song)[1:]
            item.insert(0, str(user_id))
            db.add('users', item)

            self.__song = song[1]
            self.__right = song[2]
            self.__wrong = list(song[3].split(','))

        else:
            self.__song = user[1]
            self.__right = user[2]
            self.__wrong = list(user[3].split(','))

    def get_answers(self):
        return [self.__right] + self.__wrong

    def get_song(self):
        return self.__song

    def get_right_answer(self):
        return self.__right

    def finish(self):
        db = PostgreSQL(config.database_name)
        db.delete_single('users', self.__user)

    @staticmethod
    def hasGame(user_id):
        logging.info('Checking if there is any game for user '+ str(user_id))
        db = PostgreSQL(config.database_name)
        count = db.exec_select("SELECT COUNT(*) FROM users WHERE id='"+ str(user_id)+"';")[0][0]
        print(count)
        return True if count > 0 else False
