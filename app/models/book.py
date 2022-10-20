from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.db import Base

class Book(Base):

    author = Column(String(100), nullable = False)
    book_name = Column(String(100), nullable = False)
    pages  = Column(Integer, nullable = False)
    book = relationship('Card', back_populates = 'book')
    class Config:
        orm_mode = True

