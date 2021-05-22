import logging


class User:
    # id
    # new
    # win_count
    # game_count

    def __init__(self, user_id, db):
        self.__id = user_id
        self.__new = None
        self.__win_count = None
        self.__game_count = None
        if User.exists(user_id,db):
            self.get(db)
        else:
            self.add(db)

    def getId(self):
        return self.__id

    @staticmethod
    def exists(id,db):
        logging.info("Checking if user is registered...")
        count = db.exec_select("""SELECT COUNT(*) FROM users WHERE "U_ID"=%s;""", (id,))[0][0]
        logging.debug("Count users with provided id=" + str(count))
        if count > 0:
            logging.info("User is registered.")
            return True
        else:
            logging.info("User wasn't found.")
            return False

    def add(self, db):
        logging.info("Registering a new user...")
        try:
            db.exec_update("""INSERT INTO users VALUES('%s');""", (self.__id,))
        except:
            logging.error("Can't register a user!", exc_info=True)
            return None
        self.__new = True
        self.__win_count = 0
        self.__game_count = 0
        logging.info("New user was registered.")

    def get(self, db):
        logging.info("Extract user from db...")
        try:
            user = db.exec_select("""SELECT * FROM users WHERE "U_ID"=%s;""", (self.__id,))[0]
        except:
            logging.error("User wasn't extracted from db!", exc_info=True)
            return None
        if not user or len(user) < 3:
            logging.error("User wasn't extracted from db!", exc_info=True)
            return None
        self.__new = False
        self.__win_count = user[1]
        self.__game_count = user[2]
        logging.info("User extracted.")

    def isNew(self):
        if self.__new:  # once user was checked to be new, the program knew about it at least once
            self.__new = False  # this means that it can't be considered as new any more
            return True
        else:
            return False

    def isInGame(self, db):
        logging.info("Checking if user has active game...")
        try:
            count = db.exec_select("""SELECT COUNT(*) FROM games WHERE "USER_ID"=%s;""", (self.__id,))[0][0]
            logging.debug("Count extracted from games table=" + str(count))
            if count > 0:
                logging.info("Active game found.")
                return True
            else:
                logging.info("User has no active games.")
                return False
        except:
            logging.error("Can't check whether a user have an active game!", exc_info=True)
            return False

    def addWin(self, db):
        # todo add 1 to users.WIN_COUNT and users.GAME_COUNT
        return True

    def addGame(self, db):
        # todo add 1 to users.GAME_COUNT
        return True

    # unit1- user have active game
    # unit2 - user have no active game
    # unit3 - user is not registered
    def delete(self, db):
        try:
            db.exec_update("""DELETE FROM games WHERE "USER_ID"=%s;""", (self.__id,))
            db.exec_update("""DELETE FROM users WHERE "U_ID"=%s;""", (self.__id,))
            return True
        except:
            logging.error("Can't check whether a user have an active game!", exc_info=True)
            return False
