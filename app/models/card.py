from sqlalchemy import Column, ForeignKey, Integer
from app.core.db import Base
from sqlalchemy.orm import relationship

class Card(Base):

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', back_populates = 'card')
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship('Book')
    class Config:
        orm_mode = True