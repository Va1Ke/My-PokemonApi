from pydantic import BaseModel


class PokemonUser(BaseModel):
    user_email: str
    pokemon_name: str
