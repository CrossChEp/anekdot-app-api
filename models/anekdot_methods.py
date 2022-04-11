from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from middlewares import generate_session
from schemas import AnekdotModel
from store import Anekdot


def add_anekdot_to_database(anekdot_model: AnekdotModel) -> None:
    """
    adds anekdot to database

    :param anekdot_model: AnekdotAdd
        (model of anekdot that will be posted into database
    :return: None
    """
    session = next(generate_session())
    anekdot = Anekdot(**anekdot_model.dict())
    session.add(anekdot)
    session.commit()


def get_all_anekdots_from_db() -> List[Anekdot]:
    """
    gets all anekdots from database

    :return: List[Anekdot]
    """
    session = next(generate_session())
    anekdots = session.query(Anekdot).all()
    return anekdots


def get_anekdot_from_database_by_id(anekdot_id: int) -> Anekdot:
    """
    gets concrete anekdot form database using anekdot id

    :param anekdot_id: int
        (anekdot id)
    :return: Anekdot
    """

    session: Session = next(generate_session())
    anekdot = session.query(Anekdot).filter_by(id=anekdot_id).first()
    if not anekdot:
        raise HTTPException(status_code=404, detail='anekdot not found')
    return anekdot
