from fastapi import APIRouter, HTTPException

from app.crud.library import create_user, get_user_id_by_name, \
    read_all_users_from_db, get_user_by_id, update_user, \
    get_user_id_by_mail, check_user_mail
from app.schemas.library import UserCreate, UserDB, UserUpdate


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
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User не найден')
    if obj_in.mail is not None:
        check_user_mail(obj_in.mail)
    user_update = update_user(user, obj_in)
    print(user_update)
    return user_update


@router.get('/test')
def test():
    check_user_mail('mail11')



