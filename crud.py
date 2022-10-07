import models
from database import Base, engine
from sqlalchemy.sql import text
from schemas import *
models.Base.metadata.create_all(bind=engine)

def create_book(author, book_name, pages, owner_id):
    pass

def get_all_books():
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM books')
    return rs

def create_users(name, password, pages):
    pass

def get_all_users():
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM users')
        return rs


def get_all_users():
    sql = text('SELECT * FROM users')
    result = engine.execute(sql)
    return [row for row in result]

print(get_all_users())