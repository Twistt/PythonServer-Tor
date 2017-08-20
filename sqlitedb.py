import sqlite3
#db = sqlite3.connect('data/mydb')
#create db class
# Create a database in RAM
#db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
#db = sqlite3.connect('data/mydb')
#close = db.close()


class SQLiteDB():

    db = None
    cursor = None
    def __init__(self):
        pass
        # initialization (constructor) code goes here
    def connect(self, value):
        self.db = sqlite3.connect(value)
    def sexec(self,value,tupple):
        print(value)
        self.cursor = self.db.cursor()
        self.cursor.execute(value, tupple)
        self.db.commit()
    def getone(self, value, tupple):
        self.cursor.execute(value, tupple)
        row = self.cursor.fetchone()  # retrieve the first row
        print(row)  # Print the first column retrieved(user's name)
        return row
    def getall(self,value, tupple):
        if self.cursor == None:
            self.cursor = self.db.cursor()
        self.cursor.execute(value, tupple)
        all_rows = self.cursor.fetchall()
        print(all_rows)  # Print the first column retrieved(user's name)
        return all_rows


s = SQLiteDB()
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
s.connect('teststoredb')
s.getall('select * from users;', ())

#s.sexec('drop table users;')
#s.sexec(''' CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT unique, email TEXT ,password TEXT)   ''')
#str = ('''INSERT INTO users(name, email, password) VALUES('{0}','{1}','{2}')'''.format('twist', 'test@test.com', 'tester'))
#s.sexec(str)