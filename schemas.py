from pydantic import BaseModel

class BookBase(BaseModel):
    author: str
    book_name: str | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class User(BaseModel):
    id: int
    name: str
    password: str
    mail: int

class UserCreate(UserBase):
    password: str

print(User.schema())

