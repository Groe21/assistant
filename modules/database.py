import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY,
            note TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        self.connection.commit()

    def add_note(self, note):
        self.cursor.execute("INSERT INTO notes (note) VALUES (?)", (note,))
        self.connection.commit()

    def get_notes(self):
        self.cursor.execute("SELECT * FROM notes")
        return self.cursor.fetchall()
