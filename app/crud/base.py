from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from app.core.db import SessionLocal



class CRUDBase:

    def __init__(self, model):
        self.model = model

    def get(self, obj_id):
        # получение объекта по id
        with SessionLocal() as session:
            db_obj = session.execute(
                select(self.model).where(
                    self.model.id == obj_id
                )
            )
            return  db_obj.scalars().first()

    def get_multi(self):
        # получение всех объектов из БД
        with SessionLocal() as session:
            db_objs = session.execute(select(self.model))
            db_objs = db_objs.scalars().all()
        return db_objs

    def create(self, obj_in):
        # создание объекта

        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        with SessionLocal() as session:
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj


    def update(self, db_obj, obj_in):
        # обновление данных
        # Представляем объект из БД в виде словаря.
        obj_data = jsonable_encoder(db_obj)
        # Конвертируем объект с данными из запроса в словарь,
        # исключаем неустановленные пользователем поля.
        update_data = obj_in.dict(exclude_unset=True)
        # Перебираем все ключи словаря, сформированного из БД-объекта.
        for field in obj_data:
            # Если конкретное поле есть в словаре с данными из запроса, то...
            if field in update_data:
                # ...устанавливаем объекту БД новое значение атрибута.
                setattr(db_obj, field, update_data[field])
        with SessionLocal() as session:
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
            return db_obj

    def remove(self, db_obj):
        # удаление объекта из БД
        with SessionLocal() as session:
            session.delete(db_obj)
            session.commit()
            return db_obj



