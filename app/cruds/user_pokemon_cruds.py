from fastapi import HTTPException
import databases
from sqlalchemy import and_
from app.schemas import user_pokemon_schemas, pokemon_schemas
from app.models.models import user_pokemon, pokemons


class UserPokemonCruds:
    def __init__(self, db: databases.Database):
        self.db = db

    async def check_user_has_pokemon(self, user_email: str, pokemon_name: str) -> bool:
        check = await self.db.fetch_one(user_pokemon.select().where(
            and_(user_pokemon.c.user_email == user_email, user_pokemon.c.pokemon_name == pokemon_name)))
        if check:
            return True
        return False

    async def get_user_pokemons(self, email: str, offset: int, per_page: int) -> list[pokemon_schemas.Pokemon]:
        pokemons_to_dict = await self.db.fetch_all(
            user_pokemon.select().offset(offset).limit(per_page).where(user_pokemon.c.user_email == email))
        pokemons_list = []
        for pokemon in pokemons_to_dict:
            pokemons_list.append(await self.db.fetch_one(pokemons.select().where(
                pokemons.c.name == pokemon.pokemon_name)))
        return [pokemon_schemas.Pokemon(**pokemon) for pokemon in pokemons_list]

    async def add_pokemon_to_user(self, user: user_pokemon_schemas.PokemonUser) -> HTTPException:
        check = await self.check_user_has_pokemon(user.user_email, user.pokemon_name)
        if not check:
            query = user_pokemon.insert().values(user_email=user.user_email, pokemon_name=user.pokemon_name)
            await self.db.fetch_one(query)
            return HTTPException(status_code=200, detail="Success")
        raise HTTPException(status_code=400, detail="You already have this pokemon")

    async def remove_pokemon_from_user(self, user: user_pokemon_schemas.PokemonUser) -> HTTPException:
        check = await self.check_user_has_pokemon(user.user_email, user.pokemon_name)
        if check:
            query = user_pokemon.delete().where(
                and_(user_pokemon.c.user_email == user.user_email, user_pokemon.c.pokemon_name == user.pokemon_name))
            await self.db.execute(query=query)
            return HTTPException(status_code=200, detail="Success")
        raise HTTPException(status_code=400, detail="You don't have this pokemon")
