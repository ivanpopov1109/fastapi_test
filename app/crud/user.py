from app.core.db import SessionLocal
from app.models.user import  Users
from app.schemas.user import UserCreate, UserUpdate
from typing import Optional
from sqlalchemy import select
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException


#Создание пользователя
def create_user(user: UserCreate)-> Users:
    user_data = user.dict()
    db_user = Users(**user_data)
    with SessionLocal() as session:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return db_user

# Плучить id пользователя по Имени
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

# получить список всех пользователей
def read_all_users_from_db()->list[Users]:
    with SessionLocal() as session:
        all_users = session.execute(select(Users))
        all_users = all_users.scalars().all()
    return all_users

# Получить пользователя по id
def get_user_by_id(user_id: int)-> Optional[Users]:
    with SessionLocal() as session:
        # Получаем объект класса Result.
        db_user = session.execute(
            select(Users).where(
                Users.id == user_id
            )
        )
        db_user = db_user.scalars().first()
        return db_user

# Плучить id пользователя по mail
def get_user_id_by_mail(user_mail: str) -> Optional[int]:
    with SessionLocal() as session:
        # Получаем объект класса Result.
        db_user_id = session.execute(
            select(Users.id).where(
                Users.mail == user_mail
            )
        )
        # Извлекаем из него конкретное значение.
        db_user_id = db_user_id.scalars().first()
    return db_user_id

# Обновление данных пользователя
def update_user(
        # Объект из БД для обновления
        db_user: Users,
        # ОБъект из запроса
        user_in: UserUpdate):
    # Представляем объект из БД в виде словаря.
    obj_data = jsonable_encoder(db_user)
    print(obj_data)
    # Конвертируем объект с данными из запроса в словарь,
    # исключаем неустановленные пользователем поля.
    update_data = user_in.dict(exclude_unset=True)
    print(update_data)
    # Перебираем все ключи словаря, сформированного из БД-объекта.
    for field in obj_data:
        # Если конкретное поле есть в словаре с данными из запроса, то...
        if field in update_data:
            # ...устанавливаем объекту БД новое значение атрибута.
            setattr(db_user, field, update_data[field])

    with SessionLocal() as session:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

# для обновления почты пользователя необходимо проверить его отсутсвие в БД:
def check_user_mail(user_mail:str)->None:
    user_id = get_user_id_by_mail(user_mail)
    if user_id != None:
        raise HTTPException(
            status_code=422,
            detail='Пользователь с таким email существует!',
        )

def delete_user(user: Users):
    with SessionLocal() as session:
        session.delete(user)
        session.commit()
        return user


def check_user_exists(user_id: int)->Users:
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User не найден!")
    return user

if __name__ == "__main__":
    read_all_users_from_db()
