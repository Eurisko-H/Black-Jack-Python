import os
import sqlite3
from config_log import start_logger


class DBSetup:
    def __init__(self):
        self.my_logger = start_logger()
        try:
            if not os.path.exists('db'):
                os.mkdir('db')
            self.db_path = os.path.join(os.path.dirname(__file__), 'db', 'game.db')
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            self.my_logger.info("Connected to SQLite")
        except OSError:
            self.my_logger.exception("Error while creating the file")
        except sqlite3.Error:
            self.my_logger.exception("Error while working with SQLite")

    def setup_db(self, player):
        money = player.funds - 1000
        name = player.name
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS game (
                                       name TEXT UNIQUE,
                                       win_money INTEGER NOT NULL DEFAULT 0,
                                       lost_money INTEGER NOT NULL DEFAULT 0)
                                       ;''')

        self.cursor.execute('INSERT OR IGNORE INTO game VALUES(?, ?, ?)', (name, 0, 0))
        if money >= 0:
            self.cursor.execute('UPDATE game SET win_money = win_money + ? WHERE name = ?', (abs(money), name))
        else:
            self.cursor.execute('UPDATE game SET lost_money = lost_money + ? WHERE name = ?', (abs(money), name))

        self.conn.commit()
        self.my_logger.info('values added successfully')

    def get_money(self, name):
        query = self.conn.execute('SELECT * FROM game WHERE name=:name', {'name': name})
        return query.fetchall()[0]

    def get_all_user(self):
        try:
            query = self.conn.execute('SELECT * FROM game')
            return query.fetchall()
        except sqlite3.Error:
            self.my_logger.exception("Error while working with SQLite")
            return None
