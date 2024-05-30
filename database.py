import sqlite3
from flask import g

DATABASE = 'bot_tokens.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_db():
    db = get_db()
    db.execute('''
    CREATE TABLE IF NOT EXISTS bot_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token TEXT NOT NULL
    )
    ''')
    db.commit()

def insert_token(token):
    db = get_db()
    db.execute('INSERT INTO bot_tokens (token) VALUES (?)', [token])
    db.commit()

def get_all_tokens():
    return query_db('SELECT token FROM bot_tokens')
