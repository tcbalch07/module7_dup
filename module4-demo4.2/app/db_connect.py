import pymysql
from flask import g

def get_db():
    if 'db' not in g or not is_connection_open(g.db):
        g.db = pymysql.connect(
            host='erxv1bzckceve5lh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            user='dan0jp3m1agebxgj',
            password='wq6ppnd9rbke5wrb',
            database='lhrz0tgq7zh51c6r',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

def is_connection_open(conn):
    try:
        conn.ping(reconnect=True)
        return True
    except:
        return False

def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None and not db._closed:
        db.close()