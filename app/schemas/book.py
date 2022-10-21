from pydantic import BaseModel, Field, validator
from typing import Optional


class BookBase(BaseModel):
    author: str = Field(..., min_length=1, max_length=100)
    book_name: str = Field(..., min_length=1, max_length=100)
    pages: int


class BookCreate(BookBase):
    pass


class BookDB(BookBase):
    id: int

    class Config:
        orm_mode = True


class BookUpdate(BookBase):
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    book_name: Optional[str] = Field(None, min_length=1, max_length=100)
    pages: Optional[str] = Field(None, min_length=1, max_length=100)
