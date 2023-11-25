from fastapi import HTTPException
import databases
from app.schemas import user_schemas
from app.models.models import users


class UserCruds:
    def __init__(self, db: databases.Database):
        self.db = db

    async def get_user_by_id(self, id: int) -> user_schemas.UserReturn:
        user = await self.db.fetch_one(users.select().where(users.c.user_id == id))
        if user == None:
            return None
        return user_schemas.UserReturn(user_id=user.user_id, email=user.email, password=user.password,
                                       name=user.name)

    async def get_user_by_email(self, email: str) -> user_schemas.UserReturn:
        user = await self.db.fetch_one(users.select().where(users.c.email == email))
        if user == None:
            return None
        return user_schemas.UserReturn(user_id=user.user_id, email=user.email, password=user.password, name=user.name)

    async def get_users(self, offset: int, per_page: int) -> list[user_schemas.UserReturn]:
        users_to_dict = await self.db.fetch_all(users.select().offset(offset).limit(per_page))
        return [user_schemas.UserReturn(**user) for user in users_to_dict]

    async def create_user(self, user: user_schemas.UserCreate) -> HTTPException:
        check = await self.get_user_by_email(user.email)
        if not check:
            db_user = users.insert().values(email=user.email, password=user.password, name=user.name)
            await self.db.execute(db_user)
            return HTTPException(status_code=200, detail="Success")
        raise HTTPException(status_code=400, detail="User already exist")

    async def update_user(self, new_user: user_schemas.UserCreate) -> HTTPException:
        check = await self.get_user_by_email(new_user.email)
        if check:
            query = (users.update().where(users.c.email == new_user.email).values(
                name=new_user.name, password=new_user.password, email=new_user.email,
            ))
            await self.db.execute(query=query)
            return HTTPException(status_code=200, detail="Success")
        raise HTTPException(status_code=400, detail="No such user")

    async def delete_user(self, email: str) -> HTTPException:
        check = await self.get_user_by_email(email)
        if check:
            query = users.delete().where(users.c.email == email)
            await self.db.execute(query=query)
            return HTTPException(status_code=200, detail="Success")
        raise HTTPException(status_code=400, detail="No such user")
