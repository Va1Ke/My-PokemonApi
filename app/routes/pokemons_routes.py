from fastapi import APIRouter, Query
from app.cruds.pokemon_cruds import PokemonCruds
from app.database import db


router = APIRouter()


@router.get("/pokemons/", tags=["Pokemons"])
async def get_all_pokemons(page: int = Query(1, ge=1),
                           per_page: int = Query(10, ge=1, le=25)):
    if page == 0 or per_page == 0:
        offset = 0
        per_page = 0
    else:
        offset = (page - 1) * per_page
    return await PokemonCruds(db=db).get_pokemons(offset, per_page)
