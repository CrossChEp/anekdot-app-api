from typing import List

import bcrypt
from fastapi import HTTPException
from sqlalchemy.orm import Session

from middlewares import generate_session
from models.anekdot_methods import raise_exception_if_anekdot_not_found
from schemas import UserModel, UserGetModel, UserRequestModel
from store import User


def generate_user_get_model(user: User) -> UserGetModel:
    """generates UserGetModel from User

    :param user: User
        (database object of user)
    :return: UserGetModel
    """

    user_model = UserGetModel(
        id=user.id,
        username=user.username
    )
    return user_model


def generate_user_get_model_list(users: List[User]) -> List[UserGetModel]:
    """generates list of userGetModes from list of database's user's object

    :param users: List[User]
        (list of database user's object)
    :return: List[UserGetModel]
    """

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


def is_user_in_database_exists(user: UserModel, session: Session) -> bool:
    """checks is user with nickname of user is already exists

    :param user: UserModel
        (model of user)
    :param session: Session
        (Current database session)
    :return: bool
    """
    database_user = session.query(User).filter_by(username=user.username).all()
    if database_user:
        return True
    return False


def register_user(user_data: UserModel) -> None:
    """encrypts user's password and adds him to database

    :param user_data: UserModel
        (user's data)
    :return: None
    """

    session = next(generate_session())
    if is_user_in_database_exists(user_data, session):
        raise HTTPException(status_code=405, detail='user with such nickname already exists')
    user_data.password = hash_password(user_data.password)
    user = User(**user_data.dict())
    session.add(user)
    session.commit()


def get_all_users_from_database() -> List[UserGetModel]:
    """gets all users from database

    :return: List[UserGetModel]
    """

    session = next(generate_session())
    users = session.query(User).all()
    users = generate_user_get_model_list(users)
    return users


def get_user_from_database_by_id(user_id: int) -> UserGetModel:
    """gets user from database using user's id

    :param user_id: int
        (user's id)
    :return: UserGetModel
    """

    session = next(generate_session())
    user = session.query(User).filter_by(id=user_id).first()
    raise_exception_if_anekdot_not_found(user)
    user_model = generate_user_get_model(user)
    return user_model


def get_user(user_data: UserRequestModel) -> UserGetModel:
    """gets user using UserRequestModel

    :param user_data: UserRequestModel
        (model of user)
    :return:UserGetModel
    """

    session: Session = next(generate_session())
    user_data = session.query(User).filter_by(**user_data.dict()).first()
    user_model = generate_user_get_model(user_data)
    return user_model


def get_user_private(user_data: UserRequestModel) -> User:
    """gets all user's database object, including user's password

    :param user_data: UserRequestModel
        (model of user)
    :return: User
    """

    session: Session = next(generate_session())
    user_data_without_empty_fields = clear_user_data_from_nones(user_data)
    user_data = session.query(User).filter_by(**user_data_without_empty_fields).first()
    return user_data


def clear_user_data_from_nones(user_model) -> dict:
    """deletes all empty fields from model

    :param user_model:
        (model with some fields)
    :return: dict
    """
    user_dict = {}
    for key, value in user_model.dict().items():
        if value is None:
            continue
        user_dict[key] = value
    return user_dict


