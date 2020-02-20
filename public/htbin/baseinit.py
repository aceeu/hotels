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
#default users
cursor.execute("""INSERT OR IGNORE INTO users (name, password, type) VALUES ('Admin', 'Admin', 'A')""")
cursor.execute("""INSERT OR IGNORE INTO users (name, password, type) VALUES ('{}', '{}', '{}')""".format('Manager', 'Manager', 'M'))

#hotels
cursor.execute("""
    CREATE TABLE IF NOT EXISTS hotels(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        floors INTEGER NOT NULL,
        count UNTEGER NOT NULL,
        country TEXT NOT NULL,
        city TEXT NOT NULL,
        street TEXT NOT NULL,
        house TEXT NOT NULL)
""")
cursor.execute("""INSERT OR IGNORE INTO hotels (name, floors, count, country, city, street, house) VALUES
                                                ('Cosmos',2,10,'Russia','Moscow','Lenina',2)""")
cursor.execute("""INSERT OR IGNORE INTO hotels (name, floors, count, country, city, street, house) VALUES
                                                ('First World Hotel',24,7351,'Malaysia','Genting Highlands','zzzzzz',2)""")
cursor.execute("""INSERT OR IGNORE INTO hotels (name, floors, count, country, city, street, house) VALUES
                                                ('The Venetian Resort Las Vegas',53,7092,'USA','Las Vegas','yyyyy',23)""")
cursor.execute("""INSERT OR IGNORE INTO hotels (name, floors, count, country, city, street, house) VALUES
                                                ('MGM Grand Las Vegas',30,6852,'USA','Las Vegas','fffff',1)""")

#lodgers
cursor.execute("""
    CREATE TABLE IF NOT EXISTS lodgers(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        patronymic TEXT,
        tel TEXT NOT NULL,
        passport TEXT NOT NULL,
        birthday TEXT,
        sex INTEGER NOT NULL)
""")
conn.commit()
