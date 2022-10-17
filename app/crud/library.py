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


def read_all_users_from_db()->list[Users]:
    with SessionLocal() as session:
        all_users = session.execute(select(Users))
        all_users = all_users.scalars().all()
    return all_users





if __name__ == "__main__":
    read_all_users_from_db()
