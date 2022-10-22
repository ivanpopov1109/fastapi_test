from app.core.db import SessionLocal
from app.models.user import Users
from typing import Optional
from sqlalchemy import select
from app.crud.base import CRUDBase


class CRUDUser(CRUDBase):

    # Плучить id пользователя по Имени
    def get_user_id_by_name(self, user: str) -> Optional[int]:
        with SessionLocal() as session:
            db_user_id = session.execute(
                select(Users.id).where(
                    Users.name == user
                )
            )
            db_user_id = db_user_id.scalars().first()
        return db_user_id

    # Плучить id пользователя по mail
    def get_user_id_by_mail(self, user_mail: str) -> Optional[int]:
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

user_crud = CRUDUser(Users)

if __name__ == "__main__":
    pass
