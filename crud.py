import models
from database import Base, engine
from sqlalchemy.sql import text
from schemas import *
# models.Base.metadata.create_all(bind=engine)

def create_book(author, book_name, pages, owner_id):
    pass

def get_all_books():
    sql = text('SELECT * FROM books')
    result = [row for row in engine.execute(sql) ]
    return result

def create_users(name, password, pages):
    pass


def get_all_users()->list:
    sql = text('SELECT * FROM users')
    result = [row for row in engine.execute(sql) ]
    return result

if __name__ == "__main__":
    users = get_all_users()
    print(users)
    books = get_all_books()
    print(books)