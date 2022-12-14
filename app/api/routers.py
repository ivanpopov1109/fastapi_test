from fastapi import APIRouter

from app.api.endpoints import user_router, book_router
main_router = APIRouter()
main_router.include_router(user_router, prefix='/user',
                   tags=['user'])
main_router.include_router(book_router, prefix='/book',
                   tags=['book'])
