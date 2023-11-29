from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    password: str
    email: str


class UserReturn(BaseModel):
    user_id: int
    name: str
    email: str


class UserReturnPassword(BaseModel):
    user_id: int
    name: str
    password: str
    email: str
