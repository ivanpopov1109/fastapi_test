from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.core.db import Base

class Users(Base):

    name = Column(String(100), unique = True, nullable = False)
    password = Column(String)
    mail = Column(String(50), unique = True)
    card = relationship("Card", back_populates = 'user', uselist = False, cascade = 'delete')
    class Config:
        orm_mode = True


