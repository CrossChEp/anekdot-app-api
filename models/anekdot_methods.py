from sqlalchemy.orm import Session

from middlewares import generate_session
from schemas import AnekdotAdd
from store import Anekdot


def add_anekdot_to_database(anekdot_model: AnekdotAdd) -> None:
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
