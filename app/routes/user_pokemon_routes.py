from fastapi import APIRouter, Depends, Query
from app.cruds.user_pokemon_cruds import UserPokemonCruds
from app.database import db
from app.schemas.user_pokemon_schemas import *
from app.utils.jwt_auth import get_login_from_token

router = APIRouter()


@router.get("/user-pokemons/", tags=["UserPokemons"])
async def get_all_user_pokemons(email: str, page: int = Query(1, ge=1),
                                per_page: int = Query(10, ge=1, le=25)):
    if page == 0 or per_page == 0:
        offset = 0
        per_page = 0
    else:
        offset = (page - 1) * per_page
    return await UserPokemonCruds(db=db).get_user_pokemons(email, offset, per_page)


@router.post("/add-pokemon-to-user/", tags=["UserPokemons"])
async def add_pokemon_to_user(pokemon_name: str, email_from_jwt: str = Depends(get_login_from_token)):
    return await UserPokemonCruds(db=db).add_pokemon_to_user(
        PokemonUser(user_email=email_from_jwt, pokemon_name=pokemon_name))


@router.post("/remove-pokemon-from-user/", tags=["UserPokemons"])
async def remove_pokemon_to_user(pokemon_name: str, email_from_jwt: str = Depends(get_login_from_token)):
    return await UserPokemonCruds(db=db).remove_pokemon_from_user(
        PokemonUser(user_email=email_from_jwt, pokemon_name=pokemon_name))
