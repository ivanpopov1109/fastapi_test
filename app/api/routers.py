from fastapi import APIRouter

from app.api.endpoints import user_router, book_router
main_router = APIRouter()
main_router.include_router(user_router, prefix='/library',
                   tags=['library'])
main_router.include_router(book_router, prefix='/library',
                   tags=['library'])
