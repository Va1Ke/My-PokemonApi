from fastapi import APIRouter, Depends, Query
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.cruds.user_cruds import UserCruds
from app.database import db
from app.schemas.user_schemas import *
from app.utils.jwt_auth import create_access_token, get_login_from_token, VerifyToken, token_auth_scheme, \
    refresh_access_token

router = APIRouter()


@router.post("/login/", tags=["Login"])
async def user_login(email: str, password: str):
    db_user = await UserCruds(db=db).get_user_by_email(email)
    if db_user:
        if db_user.password == password:
            response = JSONResponse(status_code=200, content={
                "access_token": create_access_token(db_user.email)
            })
            return response
        else:
            raise HTTPException(status_code=400, detail="Bad password or email")
    raise HTTPException(status_code=400, detail="No such user")


@router.post("/refresh-token/", tags=["Login"])
async def verify_token(token: str = Depends(token_auth_scheme)):
    response = JSONResponse(status_code=200, content={
        "access_token": refresh_access_token(token=token)
    })
    return response


@router.get("/user-by-email/", tags=["User"])
async def get_user_by_email(email: str):
    return await UserCruds(db=db).get_user_by_email(email)


@router.get("/users/", tags=["User"])
async def get_all_users(page: int = Query(1, ge=1),
                        per_page: int = Query(10, ge=1, le=25)):
    if page == 0 or per_page == 0:
        offset = 0
        per_page = 0
    else:
        offset = (page - 1) * per_page
    return await UserCruds(db=db).get_users(offset, per_page)


@router.post("/user/register/", tags=["User"])
async def add_user(new_user: UserCreate):
    await UserCruds(db=db).create_user(new_user)
    return {
        "result": "user added successfully"
    }


@router.put("/user/update/", tags=["User"])
async def update_user(new_user: UserCreate, email_from_jwt: str = Depends(get_login_from_token)):
    await UserCruds(db=db).update_user(new_user)
    return {
        "result": "user updated successfully"
    }


@router.delete("/user/delete/", tags=["User"])
async def delete_user(email_from_jwt: str = Depends(get_login_from_token)):
    await UserCruds(db=db).delete_user(email_from_jwt)
    return {
        "result": "user deleted successfully"
    }
