import psycopg2
import config
import logging
import os

class PostgreSQL:
    def __init__(self, database):
        try:
            postgre_conn_string = os.getenv('DB_CONNECTION', '')
            self.conn = psycopg2.connect(config.postgre_conn_string)
        except Exception as e:
            logging.error('Connection to db failed')
            logging.error('Exception occurred', exc_info=True)
        self.cursor = self.conn.cursor()

# todo replace with count(*)
    def count_rows(self, table):
        self.cursor.execute('SELECT * FROM ' + table)
        result = self.cursor.fetchall()
        return len(result)

    def delete_all(self, table):
        self.cursor.execute("""DELETE FROM """ + table + """;""")
        self.conn.commit()

    def exec_select(self, sql,parms):
        self.cursor.execute(sql,parms)
        res = self.cursor.fetchall()
        self.conn.commit()
        return res

#todo describe how parms must be passed here
    def exec_update(self, sql, parms):
        self.cursor.execute(sql,parms)
        self.conn.commit()

    def close(self):
        self.cursor.close()

