import bcrypt

from middlewares import generate_session
from schemas import UserModel
from store import User


def hash_password(password: str) -> bytes:
    hashed_password = bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())
    return hashed_password


def register_user(user_data: UserModel) -> None:
    session = next(generate_session())
    user_data.password = hash_password(user_data.password)
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
