import sqlite3
from datetime import datetime
import os

def initiate_db():
    global conn, c
    conn = sqlite3.connect("db.db")
    c = conn.cursor()


def initiate_table():
    statement = """CREATE TABLE password
                  (platform text primary key,
                   username text,
                   passhash text,
                   datetime text)"""

    c.execute(statement)
    conn.commit()


def add(platform, username, passhash):
    initiate_db()
    dt = datetime.now()
    c.execute("INSERT INTO password VALUES(?,?,?,?)", (platform, username, passhash, dt))
    conn.commit()


def retrieve(platform):
    initiate_db()
    c.execute("SELECT * FROM password WHERE platform = ?", (platform,))
    data = c.fetchone()
    return data


def delete(platform):
    initiate_db()
    c.execute("DELETE FROM password WHERE platform = ?", (platform,))
    conn.commit()


def names():
    initiate_db()
    c.execute("SELECT platform FROM password")
    data = c.fetchall()
    for i in range(len(data)):
        data[i] = data[i][0]
    return data


if __name__ == "__main__":
    os.chdir("bin")
    print(names())
