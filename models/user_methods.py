from typing import List

import bcrypt

from middlewares import generate_session
from models.anekdot_methods import raise_exception_if_anekdot_not_found
from schemas import UserModel, UserGetModel
from store import User


def generate_user_get_model(user: User) -> UserGetModel:
    user_model = UserGetModel(
        id=user.id,
        username=user.username
    )
    return user_model


def generate_user_get_model_list(users: List[User]) -> List[UserGetModel]:
    user_models = []
    for user in users:
        user_model = generate_user_get_model(user)
        user_models.append(user_model)
    return user_models


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


def get_all_users_from_database() -> List[UserGetModel]:
    session = next(generate_session())
    users = session.query(User).all()
    users = generate_user_get_model_list(users)
    return users


def get_user_from_database_by_id(user_id: int) -> UserGetModel:
    session = next(generate_session())
    user = session.query(User).filter_by(id=user_id).first()
    raise_exception_if_anekdot_not_found(user)
    user_model = generate_user_get_model(user)
    return user_model
