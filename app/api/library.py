from fastapi import APIRouter, HTTPException

from app.crud.library import create_user, get_user_id_by_name
from app.schemas.library import UserCreate

router = APIRouter()

@router.post('/users/')
def create_new_user(
        user: UserCreate,
):

    user_id = get_user_id_by_name(user.name)
    if user_id is not None:
        raise HTTPException(status_code=422,
                            detail='Пользователь с таким именем существует')
    new_user = create_user(user)
    return new_user




