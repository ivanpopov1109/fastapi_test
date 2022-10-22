from fastapi import APIRouter
from app.schemas.book import BookCreate, BookDB, BookUpdate
from app.crud.book import book_crud
from app.api.validators import check_book_exists

router = APIRouter()


@router.post('/book/',
             response_model=BookDB,
             response_model_exclude_none=True)
def create_new_book(book: BookCreate):
    new_book = book_crud.create(book)
    return new_book


@router.get('/book/',
            response_model=list[BookDB],
            response_model_exclude_none=True)
def get_all_book():
    all_book = book_crud.get_multi()
    return all_book


@router.patch('/{book_id}')
def partially_update_book(book_id: int, book_in: BookDB):
    book = check_book_exists(book_id)
    book_update = book_crud.update(book, book_in)
    return book_update


@router.delete('/{book_id}',
               response_model=BookDB,
               response_model_exclude_none=True)
def remove_book(book_id: int):
    print(book_id)
    book = check_book_exists(book_id)
    print(book)
    book = book_crud.remove(book)
    return book
