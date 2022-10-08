from fastapi import  FastAPI

from crud import get_all_books, get_all_users, new_book, new_user, get_user
from schemas import *


app = FastAPI()

@app.post('/create_user/')
def create_user(user: UserBase):
    new_user(user)


@app.post('/create_book/')
def create_book(book: BookBase):
    new_book(book)

@app.get('/books/')
def books():
    res = get_all_books()
    return res

@app.get('/users/')
def users():
    res = get_all_users()
    return res

@app.get('/users/{id}')
def user(id:int):
    res = get_user(id)
    return res


