

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.db import Base

from app.core.db import Base

class Users(Base):

    name = Column(String(100), unique = True, nullable = False)
    password = Column(String)
    mail = Column(String(50), unique = True)
    books = relationship("Books", back_populates="owner")
    class Config:
        orm_mode = True

class Books(Base):

    author = Column(String(100), nullable = False)
    book_name = Column(String(100), nullable = False)
    pages  = Column(Integer, nullable = False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("Users", back_populates="books")


