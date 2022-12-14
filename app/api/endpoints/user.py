from fastapi import APIRouter, HTTPException
from app.crud.user import user_crud
from app.schemas.user import UserCreate, UserDB, UserUpdate
from app.crud.book import book_crud
from app.schemas.book import *
from app.api.validators import check_user_exists, check_user_mail


router = APIRouter()

@router.post('/user/',
             response_model= UserDB,
             response_model_exclude_none=True)
def create_new_user(user: UserCreate):
    user_id = user_crud.get_user_id_by_name(user.name)
    if user_id is not None:
        raise HTTPException(status_code=422,
                            detail='Пользователь с таким именем существует')
    new_user = user_crud.create(user)
    return new_user

@router.get('/user/', response_model=list[UserDB],
            response_model_exclude_none=True)
def get_all_users():
    all_users = user_crud.get_multi()
    return all_users

@router.patch('/{user_id}')
def partially_update_user(user_id: int, obj_in: UserUpdate):
    user = check_user_exists(user_id)
    if obj_in.mail is not None:
        check_user_mail(obj_in.mail)
    user_update = user_crud.update(user, obj_in)
    return user_update

@router.delete('/{user_id}',
               response_model=UserDB,
               response_model_exclude_none= True)
def remove_user(user_id: int):
    print(user_id)
    user = check_user_exists(user_id)
    user = user_crud.remove(user)
    return user







