from sqlalchemy import create_engine, Column, Integer
from app.core.config import settings
from sqlalchemy.orm import sessionmaker, declarative_base, Session, declared_attr

class PreBase:
    @declared_attr
    def __tablename__(cls):
        # Именем таблицы будет название модели в нижнем регистре.
        return cls.__name__.lower()
    # Во все таблицы будет добавлено поле ID.
    id = Column(Integer, primary_key=True)



# создадим движок, передадим url из конфига
engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(engine, class_= Session)

# базовый класс будущих моделей
# В качестве основы для базового класса укажем класс PreBase
Base = declarative_base(cls=PreBase)