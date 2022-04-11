from typing import List

from fastapi import APIRouter

from models import register_user, get_all_users_from_database, get_user_from_database_by_id
from schemas import UserModel, UserGetModel
from store import User

user_router = APIRouter()


@user_router.post('/api/register')
def register(user_data: UserModel):
    register_user(user_data)


@user_router.get('/api/users')
def get_users() -> List[UserGetModel]:
    return get_all_users_from_database()


@user_router.get('/api/user/{id}')
def get_user_by_id(user_id: int) -> UserGetModel:
    return get_user_from_database_by_id(user_id)
