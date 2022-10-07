from fastapi import  FastAPI
from pydantic import BaseModel
from crud import get_all_books, get_all_users


app = FastAPI()

class BookShema(BaseModel):
    title: int
    description: str

class UserSchema(BaseModel):
    email: str
    hashed_password: str
    is_active: bool


@app.post('/user')
def create_user(user: UserSchema):
    return user

@app.get('/book', response_model=list[BookShema])
def create_book(book: BookShema):
    return book

@app.get('/books')
def get_all_books():
    return books



