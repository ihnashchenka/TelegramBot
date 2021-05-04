import psycopg2
import config
import logging

class PostgreSQL:
    def __init__(self, database):
        try:
            self.conn = psycopg2.connect(config.postgre_conn_string)
        except Exception as e:
            logging.error('Connection to db failed')
            logging.error('Exception occurred', exc_info=True)
        self.cursor = self.conn.cursor()

    def select_all(self,table):
        self.cursor.execute('SELECT * FROM '+table)
        res = self.cursor.fetchall()
        return res

    def select_single(self, table, rownum):
        self.cursor.execute("""SELECT * FROM """+table + """ WHERE id='%s'""", (rownum,))
        item = self.cursor.fetchall()
        if item:
            return item[0]
        return None

    def count_rows(self, table):
        self.cursor.execute('SELECT * FROM ' + table)
        result = self.cursor.fetchall()
        return len(result)

    def add(self, table, item):
        self.cursor = self.conn.cursor()
        length = len(item)
        str = ''
        for i in range(length):
            str = str + "%s, "
        str = str[:-2]
        self.cursor.execute("INSERT INTO " + table + "(id, file_id, right_answer, wrong_answer) VALUES(" + str + ")", (item))
        self.cursor.close()
        self.conn.commit()

    def delete_single(self, table, rownum):
        self.cursor.execute("""DELETE FROM """ + table + """ WHERE id='%s'""", (rownum,))
        self.cursor.close()
        self.conn.commit()

    def delete_all(self, table):
        self.cursor.execute("""DELETE FROM """ + table + """;""")
        self.cursor.close()
        self.conn.commit()

    def exec_select(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.cursor.close()
        self.conn.commit()
        return res

