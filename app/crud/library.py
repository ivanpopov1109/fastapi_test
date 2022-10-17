from app.core.db import engine, SessionLocal
from sqlalchemy.sql import text
from app.models.library import Books, Users
from app.schemas.library import BookCreate, UserCreate
from typing import Optional
from sqlalchemy import select


# def new_user(user):
#     with engine.connect() as con:
#         con.execute('INSERT INTO users (id, name, password, mail ) values ( :id, :name,:password, :mail)',
#                     (user.id, user.name, user.password, user.mail))
#         con.close()

def create_user(user: UserCreate):
    user_data = user.dict()
    db_user = Users(**user_data)
    with SessionLocal() as session:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return db_user

def get_user_id_by_name(user: str) -> Optional[int]:
    with SessionLocal() as session:
        # Получаем объект класса Result.
        db_user_id = session.execute(
            select(Users.id).where(
                Users.name == user
            )
        )
        # Извлекаем из него конкретное значение.
        db_user_id = db_user_id.scalars().first()
    return db_user_id
# def new_book(book):
#     with engine.connect() as con:
#         con.execute('INSERT INTO books values ( :id, :author,:book_name, :pages, :owner_id)',
#                     (book.id, book.author, book.book_name , book.pages, book.owner_id))
#         con.close()
#
#
# def get_all_books():
#     sql = text('SELECT * FROM books')
#     result = [row for row in engine.execute(sql)]
#     return result
#
# def get_all_users() -> list:
#     sql = text('SELECT * FROM users')
#     result = [row for row in engine.execute(sql)]
#     return result
#
# def get_user(id)-> list:
#     with engine.connect() as con:
#         res = con.execute('SELECT * FROM users WHERE id = :id', id)
#         res = [i for i in res]
#     return res
#
# def get_users_book(id)->list:
#     with engine.connect() as con:
#         res = con.execute('SELECT * FROM users WHERE id = :id', id)
#         res = [i for i in res]
#     return res


if __name__ == "__main__":
    res = get_user(1)
    for row in res:
        print(row)

