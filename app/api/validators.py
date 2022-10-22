from app.models.user import Users
from app.models.book import Book
from fastapi import HTTPException
from app.crud.user import user_crud
from app.crud.book import book_crud


def check_user_exists(user_id: int) -> Users:
    user = user_crud.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User не найден!")
    return user


def check_user_mail(user_mail: str) -> None:
    user_id = user_crud.get_user_id_by_mail(user_mail)
    if user_id != None:
        raise HTTPException(
            status_code=422,
            detail='Пользователь с таким email существует!',
        )

def check_user_exists(user_id: int) -> Users:
    user = user_crud.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User не найден!")
    return user

def check_book_exists(book_id: int) -> Book:
    book = book_crud.get(book_id)
    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book не найден!")
    return book
