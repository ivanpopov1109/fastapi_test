from fastapi import  FastAPI
from app.core.config import settings
from app.crud.library import get_all_books, get_all_users, new_book, new_user, get_user
from app.schemas.library import *

app = FastAPI(title=settings.app_title,
              description=settings.description)

@app.post('/create_user/',
          summary='Создание пользователя')
def create_user(user: UserBase):
    new_user(user)


@app.post('/create_book/',
          summary='Создание книги'
          )
def create_book(book: BookBase):
    new_book(book)

@app.get('/books/',
         summary='Список кнег',
         response_description='Все книги')
def books():
    res = get_all_books()
    return res

@app.get('/users/', summary='Списко пользователей',
         response_description='Все пользователи')
def users():
    res = get_all_users()
    return res

@app.get('/users/{id}')
def user(id:int):
    res = get_user(id)
    return res


