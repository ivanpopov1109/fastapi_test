from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
'''создадим url бд'''
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

'''создадим движок бд'''
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
'''создадим сеанс подключения к бд'''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

'''создадим родительский класс БД(???) От которого потом будут наследоваться модели'''
Base = declarative_base()