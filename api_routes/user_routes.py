from fastapi import APIRouter

from models import register_user
from schemas import UserModel

user_router = APIRouter()


@user_router.post('/api/register')
def register(user_data: UserModel):
    register_user(user_data)
