import sqlite3
import os
 
path = os.path.dirname(os.path.abspath(__file__))
hotelsfilename = os.path.join(path, 'hotels.db')

conn = sqlite3.connect(hotelsfilename)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    type TEXT NOT NULL,
    hotelId INTEGER
    )""")
cursor.execute("""INSERT OR IGNORE INTO users (name, password, type) VALUES ('Admin', 'Admin', 'A')""")
cursor.execute("""INSERT OR IGNORE INTO users (name, password, type) VALUES ('{}', '{}', '{}')""".format('Manager', 'Manager', 'M'))

#hotels
cursor.execute("""
    CREATE TABLE IF NOT EXISTS hotels(
        id INTEGER PRIMARY KEY,
        floors INTEGER NOT NULL,
        count UNTEGER NOT NULL,
        country TEXT NOT NULL,
        city TEXT NOT NULL,
        street TEXT NOT NULL,
        house TEXT NOT NULL)
""")
conn.commit()