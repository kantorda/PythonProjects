import sqlite3


class Person:
    def __init__(self):
        self.name = ''
        self.age = ''

class Database:
    def __init__(self):
        self.con = sqlite3.connect('UserDatabase.db')
        self.cur = self.con.cursor()

    def init_table(self):
        self.cur.execute('CREATE TABLE users (name text, age real)')

    def add(self, name, age):
        self.cur.execute('INSERT INTO users VALUES (?, ?)', (name, age))

    def find(self, name):
        for row in self.cur.execute('SELECT * FROM users WHERE name=?', [name]):
            print(row)

    def remove(self, name):
        self.cur.execute('DELETE FROM users WHERE name=?', [name])

    def print_all(self):
         for row in self.cur.execute('SELECT * FROM users'):
            print(row)


if __name__ == "__main__":
    database = Database()

    database.cur.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users' ''')
    if database.cur.fetchone()[0] == 0 :
        database.init_table()
        database.add('Paul', 27)
        database.add('Dorothy', 43)
        database.add('Randy', 33)
        database.add('Mike', 17)
        database.add('Jessica', 18)
        database.add('Mike', 58)

    database.find('Paul')
    database.find('Dorothy')
    database.find('Mike')

    database.print_all()

    database.remove('Mike')
    database.print_all()

    database.con.commit()
    database.con.close()