import bcrypt

from middlewares import generate_session
from schemas import UserModel
from store import User


def hash_password(password: str) -> bytes:
    """hashes password

    :param password: str
        (user's input password)
    :return: bytes
    """

    hashed_password = bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())
    return hashed_password


def register_user(user_data: UserModel) -> None:
    """encrypts user's password and adds him to database

    :param user_data: UserModel
        (user's data)
    :return: None
    """

    session = next(generate_session())
    user_data.password = hash_password(user_data.password)
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
