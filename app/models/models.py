from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)


users = User.__table__


class UserPokemon(Base):
    __tablename__ = "user_pokemon"
    record_id = Column(Integer, primary_key=True, index=True, unique=True)
    user_email = Column(String, ForeignKey('users.email', ondelete='CASCADE'))
    pokemon_name = Column(String, ForeignKey('pokemons.name', ondelete='CASCADE'))

    users = relationship('User', backref='user_pokemon', cascade='all,delete')
    pokemons = relationship('Pokemon', backref='user_pokemon', cascade='all,delete')


user_pokemon = UserPokemon.__table__


class Pokemon(Base):
    __tablename__ = "pokemons"
    pokemon_id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False, unique=True)
    hp = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    special_attack = Column(Integer, nullable=False)
    special_defense = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)


pokemons = Pokemon.__table__
