from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from middlewares import generate_session
from models import add_anekdot_to_database
from schemas import AnekdotAdd

anekdot_route = APIRouter()


@anekdot_route.post('/api/anekdot')
def post_anekdot(anekdot_model: AnekdotAdd) -> None:
    add_anekdot_to_database(anekdot_model)
