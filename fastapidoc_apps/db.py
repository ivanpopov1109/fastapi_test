#
#
# class Some_db:
#
#     database = {}
#     _pk = 0
#     @classmethod
#     def put_db(cls, x1, x2):
#         Some_db._pk+=1
#         Some_db.database[Some_db._pk] = f'{x1}*{x2} = {x1*x2}'
#
#     @classmethod
#     def get(self):
#         return Some_db.database
#
#     @classmethod
#     def delete(self, pk):
#         if pk in Some_db.database.keys():
#             del Some_db.database[pk]
#
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
) # движок для базы
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

