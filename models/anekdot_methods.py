import random
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from middlewares import generate_session
from schemas import AnekdotModel, AnekdotUpdateModel
from store import Anekdot, User


def raise_exception_if_anekdot_not_found(anekdot):
    if not anekdot:
        raise HTTPException(status_code=404, detail='not found')


def add_anekdot_to_database(anekdot_model: AnekdotModel, author: User) -> None:
    """adds anekdot to database

    :param anekdot_model: AnekdotAdd
        (model of anekdot that will be posted into database
    :param author: User
        (future author of anekdot)
    :return: None
    """
    session = next(generate_session())
    anekdot = Anekdot(**anekdot_model.dict())
    author.anekdots.append(anekdot)
    current_session = session.object_session(anekdot)
    current_session.add(anekdot)
    current_session.commit()


def get_all_anekdots_from_db() -> List[Anekdot]:
    """gets all anekdots from database

    :return: List[Anekdot]
    """
    session = next(generate_session())
    anekdots = session.query(Anekdot).all()
    return anekdots


def get_anekdot_from_database_by_id(anekdot_id: int) -> Anekdot:
    """gets concrete anekdot form database using anekdot id

    :param anekdot_id: int
        (anekdot id)
    :return: Anekdot
    """

    session: Session = next(generate_session())
    anekdot = session.query(Anekdot).filter_by(id=anekdot_id).first()
    raise_exception_if_anekdot_not_found(anekdot)
    return anekdot


def get_random_anekdot_from_database() -> Anekdot:
    """gets random anekdot from database

    :return: Anekdot
    """

    session: Session = next(generate_session())
    all_anekdots = session.query(Anekdot).all()
    raise_exception_if_anekdot_not_found(all_anekdots)
    random_anekdot_id = random.randint(1, len(all_anekdots))
    random_anekdot = get_anekdot_from_database_by_id(random_anekdot_id)
    return random_anekdot


def delete_anekdot_from_database_by_id(anekdot_id: int) -> None:
    """deletes anekdot from database

    :param anekdot_id: int
        (anekdot id)
    :return: None
    """

    session: Session = next(generate_session())
    anekdot = session.query(Anekdot).filter_by(id=anekdot_id).first()
    raise_exception_if_anekdot_not_found(anekdot)
    session.delete(anekdot)
    session.commit()


def update_anekdot_in_database(anekdot_model: AnekdotUpdateModel) -> None:
    """Updates anekdot's content

    :param anekdot_model: AnekdotUpdateModel
        (update model of anekdot)
    :return: None
    """

    session: Session = next(generate_session())
    anekdot: Anekdot = session.query(Anekdot).filter_by(id=anekdot_model.id).first()
    raise_exception_if_anekdot_not_found(anekdot)
    anekdot.content = anekdot_model.content
    session.commit()

