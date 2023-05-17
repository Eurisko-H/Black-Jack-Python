import os
import sqlite3


class DBSetup:
    def __init__(self):
        try:
            if not os.path.exists('db'):
                os.mkdir('db')
            self.db_path = os.path.join(os.path.dirname(__file__), 'db', 'game.db')
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            print("Connected to SQLite")
        except OSError as error:
            print("Error while creating the file", error)
        except sqlite3.Error as error:
            print("Error while working with SQLite", error)

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
        print('values added successfully')

    def get_money(self, name):
        query = self.conn.execute('SELECT * FROM game WHERE name=:name', {'name': name})
        return query.fetchall()[0]

    def get_all_user(self):
        query = self.conn.execute('SELECT * FROM game')
        return query.fetchall()
