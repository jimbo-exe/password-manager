import sqlite3
from datetime import datetime

conn = sqlite3.connect(":memory:")
c = conn.cursor()


def initiate():
    statement = """CREATE TABLE password
                  (platform text primary key,
                   username text,
                   passhash text,
                   datetime text)"""

    c.execute(statement)
    conn.commit()


def add(platform, username, passhash):
    dt = datetime.now()
    c.execute("INSERT INTO password VALUES(?,?,?,?)", (platform, username, passhash, dt))
    conn.commit()


def retrieve(platform):
    c.execute("SELECT * FROM password WHERE platform = ?", (platform,))
    data = c.fetchone()
    return data


def delete(platform):
    c.execute("DELETE FROM password WHERE platform = ?", (platform,))
    conn.commit()


def names():
    c.execute("SELECT platform FROM password")
    data = c.fetchall()
    return data


if __name__ == "__main":
    print(names())