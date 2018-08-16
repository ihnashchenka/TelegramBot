from PostgreSQL import PostgreSQL
import config


def is_in_game(user_id):
    db = PostgreSQL(config.database_name)
    if db.select_single('users', user_id):
        return True
    return False

