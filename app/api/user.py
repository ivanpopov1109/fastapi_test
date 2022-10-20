from fastapi import APIRouter, HTTPException

from app.crud.user import create_user, get_user_id_by_name, \
    read_all_users_from_db, get_user_by_id, update_user, \
    get_user_id_by_mail, check_user_mail, delete_user, check_user_exists
from app.schemas.user import UserCreate, UserDB, UserUpdate
from app.models.user import Users


router = APIRouter(prefix='/library',
                   tags=['library'])

@router.post('/users/',
             response_model= UserDB,
             response_model_exclude_none=True)
def create_new_user(user: UserCreate):
    user_id = get_user_id_by_name(user.name)
    if user_id is not None:
        raise HTTPException(status_code=422,
                            detail='Пользователь с таким именем существует')
    new_user = create_user(user)
    return new_user

@router.get('/users/', response_model=list[UserDB],
            response_model_exclude_none=True)
def get_all_users():
    all_users = read_all_users_from_db()
    return all_users

@router.patch('/{user_id}')
def partially_update_user(user_id: int, obj_in: UserUpdate):
    user = check_user_exists(user_id)
    if obj_in.mail is not None:
        check_user_mail(obj_in.mail)
    user_update = update_user(user, obj_in)
    print(user_update)
    return user_update

@router.delete('/{user_id}', response_model=UserDB, response_model_exclude_none= True)
def remove_user(user_id: int):
    user = check_user_exists(user_id)
    user = delete_user(user)
    return user

@router.get('/test')
def test():
    check_user_mail('mail11')



