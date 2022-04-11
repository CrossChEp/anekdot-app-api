from typing import List

from fastapi import APIRouter
from models import add_anekdot_to_database, get_all_anekdots_from_db, get_anekdot_from_database_by_id, \
    get_random_anekdot_from_database, delete_anekdot_from_database_by_id, update_anekdot_in_database
from schemas import AnekdotModel, AnekdotUpdateModel
from store import Anekdot

anekdot_route = APIRouter()


@anekdot_route.post('/api/anekdot')
def post_anekdot(anekdot_model: AnekdotModel) -> None:
    add_anekdot_to_database(anekdot_model)


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
def delete_anekdot(anekdot_id: int) -> None:
    delete_anekdot_from_database_by_id(anekdot_id)


@anekdot_route.put('/api/anekdot/')
def update_anekdot(anekdot_model: AnekdotUpdateModel) -> None:
    update_anekdot_in_database(anekdot_model)
