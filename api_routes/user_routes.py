from fastapi import APIRouter

from schemas import UserModel

user_router = APIRouter()


@user_router.post('/api/register')
def register(user_data: UserModel):
    pass
