from pydantic import BaseModel, Field
from typing import Optional


class BookCreate(BaseModel):
    author: str = Field(..., min_length=1, max_length=100)
    book_name: str = Field(..., min_length=1, max_length=100)
    pages: int
    owner_id: int


class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    mail: str = Field(..., min_length=1, max_length=100)


class UserCreate(UserBase):
    password: str = Field(..., min_length=1, max_length=100)


class UserDB(UserBase):
    id: int
    mail: Optional[str]

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    password: Optional[str] = Field(None, min_length=1, max_length=100)
    name: Optional[str] = Field(None,  min_length=1, max_length=100)
    mail: Optional[str] = Field(None, min_length=1, max_length=100)

if __name__ == "__main__":
    pass
