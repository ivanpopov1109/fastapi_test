import models
from database import Base, engine
from sqlalchemy.sql import text
from schemas import *


# models.Base.metadata.create_all(bind=engine)

def new_book(book):
    with engine.connect() as con:
        con.execute('INSERT INTO books values ( :id, :author,:book_name, :pages, :owner_id)',
                    (book.id, book.author, book.book_name , book.pages, book.owner_id))
        con.close()


def get_all_books():
    sql = text('SELECT * FROM books')
    result = [row for row in engine.execute(sql)]
    return result


def new_user(user):
    with engine.connect() as con:
        con.execute('INSERT INTO users (id, name, password, mail ) values ( :id, :name,:password, :mail)',
                    (user.id, user.name, user.password, user.mail))
        con.close()


def get_all_users() -> list:
    sql = text('SELECT * FROM users')
    result = [row for row in engine.execute(sql)]
    return result

def get_user(id)-> list:
    with engine.connect() as con:
        res = con.execute('SELECT * FROM users WHERE id = :id', id)
        res = [i for i in res]
    return res

def get_users_book(id)->list:
    with engine.connect() as con:
        res = con.execute('SELECT * FROM users WHERE id = :id', id)
        res = [i for i in res]
    return res


if __name__ == "__main__":
    res = get_user(1)
    for row in res:
        print(row)

