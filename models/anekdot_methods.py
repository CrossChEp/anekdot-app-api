import random
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from middlewares import generate_session
from schemas import AnekdotModel
from store import Anekdot


def add_anekdot_to_database(anekdot_model: AnekdotModel) -> None:
    """adds anekdot to database

    :param anekdot_model: AnekdotAdd
        (model of anekdot that will be posted into database
    :return: None
    """
    session = next(generate_session())
    anekdot = Anekdot(**anekdot_model.dict())
    session.add(anekdot)
    session.commit()


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
    if not anekdot:
        raise HTTPException(status_code=404, detail='anekdot not found')
    return anekdot


def get_random_anekdot_from_database() -> Anekdot:
    """gets random anekdot from database

    :return: Anekdot
    """

    session: Session = next(generate_session())
    all_anekdots = session.query(Anekdot).all()
    if not all_anekdots:
        raise HTTPException(status_code=404, detail='anekdot list is empty')
    random_anekdot_id = random.randint(1, len(all_anekdots))
    random_anekdot = get_anekdot_from_database_by_id(random_anekdot_id)
    return random_anekdot
