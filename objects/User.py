import logging

class User:
    #id
    #new
    #win_count
    #game_count

    def __init__(self, user_id,db):
        self.__id=user_id
        self.__new=None
        self.__win_count=None
        self.__game_count=None
        if self.exists(db):
           self.get(db)
        else:
            self.add(db)

    def getId(self):
        return self.__id

    def exists(self,db):
        logging.info("Checking if user is registered...")
        count = db.exec_select("""SELECT COUNT(*) FROM users WHERE "U_ID"=%s;""", (self.__id,))[0][0]
        print(count)

        if count > 0:
            logging.info("User is registered.")
            return True
        else:
            logging.info("User wasn't found.")
            return False

    def add(self,db):
            logging.info("Regestring new user...")
            try:
                db.exec_insert("""INSERT INTO users VALUES('%s');""", (self.__id,))
            except:
                logging.error("Can't regester a user!",exc_info=True)
                return None
            self.new=True
            self.__win_count=0
            self.__game_count=0
            logging.info("New user was registered.")

    def get(self,db):
        try:
            logging.info("Extract user from db...")
            user = db.exec_select("""SELECT * FROM users WHERE "U_ID"=%s;""", (self.__id,))[0]
        except:
            logging.error("User wasn't extracted from db!",exc_info=True)
            return None
        if not user or len(user)<3:
            logging.error("User wasn't extracted from db!", exc_info=True)
            return None
        self.__new=False
        self.__win_count=user[1]
        self.__game_count=user[2]
        logging.info("User extracted.")

#once user was chacked to be new, the program knew about it at least once
#this means that it can'tbe considered as new any more

    def isNew(self): #can be changed to game_count check - if it is more that 0 than the user isn't new.
        if self.__new:
            self.__new=False
            return True
        else:
            return False

    def isInGame(self,db):
        logging.info("Checking if user has active game...")
        try:
            count = db.exec_select("""SELECT COUNT(*) FROM games WHERE "USER_ID"=%s;""", (self.__id,))[0][0]
            logging.debug("Count extracted from games table="+str(count))
            if count > 0:
                logging.info("Active game found.")
                return True
            else:
                logging.info("User has no active games.")
                return False
        except:
            logging.error("Can't check whether a user have an active game!",exc_info=True)
            return False

    def addWin(self,db):
        return True

    def addGame(self,db):
        #add 1 to GAME_COUNT
        return True






