import databases
from app.schemas import pokemon_schemas
from app.models.models import pokemons


class PokemonCruds:
    def __init__(self, db: databases.Database):
        self.db = db

    async def get_pokemons(self, offset: int, per_page: int) -> list[pokemon_schemas.Pokemon]:
        pokemons_to_dict = await self.db.fetch_all(pokemons.select().offset(offset).limit(per_page))
        return [pokemon_schemas.Pokemon(**pokemon) for pokemon in pokemons_to_dict]
