from PostgreSQL import PostgreSQL
import config
import random

class Game:
    def __init__(self, user_id):
        db = PostgreSQL(config.database_name)
        self.__user = user_id
        user = db.select_single('users', user_id)

        if not user:
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
