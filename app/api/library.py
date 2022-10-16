from fastapi import APIRouter

from app.crud.library import create_user
from app.schemas.library import UserCreate

router = APIRouter()

@router.post('/users/')
def create_new_user(
        user: UserCreate,
):
    print(user)
    new_user = create_user(user)
    return new_user


