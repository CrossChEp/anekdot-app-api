from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api_routes.auth_router import get_current_user
from middlewares import generate_session
from models import add_anekdot_to_database, get_all_anekdots_from_db, get_anekdot_from_database_by_id, \
    get_random_anekdot_from_database, delete_anekdot_from_database_by_id, update_anekdot_in_database, \
    add_anekdot_to_liked
from schemas import AnekdotModel, AnekdotUpdateModel
from store import Anekdot, User

anekdot_route = APIRouter()


@anekdot_route.post('/api/anekdot')
def post_anekdot(anekdot_model: AnekdotModel, author: User = Depends(get_current_user)) -> None:
    add_anekdot_to_database(anekdot_model, author)


@anekdot_route.get('/api/anekdots')
def get_anekdots() -> List[Anekdot]:
    return get_all_anekdots_from_db()


@anekdot_route.get('/api/anekdot/{anekdot_id}')
def get_concrete_anekdot(anekdot_id: int) -> Anekdot:
    return get_anekdot_from_database_by_id(anekdot_id)


@anekdot_route.get('/api/anekdots/random')
def get_random_anekdot() -> Anekdot:
    return get_random_anekdot_from_database()


@anekdot_route.delete('/api/anekdot/{anekdot_id}')
def delete_anekdot(anekdot_id: int, author: User = Depends(get_current_user)) -> None:
    delete_anekdot_from_database_by_id(anekdot_id, author)


@anekdot_route.put('/api/anekdot/')
def update_anekdot(anekdot_model: AnekdotUpdateModel, author: User = Depends(get_current_user)) -> None:
    update_anekdot_in_database(anekdot_model, author)


@anekdot_route.post('/api/anekdot/like/{anekdot_id}')
def like_anekdot(anekdot_id: int, current_user: User = Depends(get_current_user)):
    add_anekdot_to_liked(current_user=current_user, anekdot_id=anekdot_id)
