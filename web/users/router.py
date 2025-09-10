from datetime import datetime
from fastapi import APIRouter, Query, Request, Response, Depends
from typing import Annotated, Sequence, Optional, Any

from web.users.dependencies import get_current_user, get_token
from web.users.models import UserModel
from web.users.schema import User, UserLogin, UserReg, UserSearch
from web.users.dao import UsersDAO
from web.exceptions import UserExistException
from web.users.auth import auth_user, create_token, get_pass_hash

router = APIRouter(prefix="/users", tags=["Users", "Auth"])

@router.get("")
async def get_all_users(filter_query: Annotated[UserSearch, Query()]) -> Sequence[User]:
    """
    Get all users
    """
    filter_model = filter_query.model_dump(exclude_unset=True, exclude_defaults=True) 
    return await UsersDAO.find_all(**filter_model)
    
# @router.get("/one_model_or_list")
# async def get_all_users(filter_query: Annotated[UserSearch, Query()]) -> Sequence[User] | User:
#     """
#     Get all users with single model
#     """
#     filter_model = filter_query.model_dump(exclude_unset=True, exclude_defaults=True) 
#     return await UsersDAO.find(**filter_model)


@router.post("/register", status_code=201)
async def register_user(user_data: UserReg):
    existing_user = await UsersDAO.find_one(email=user_data.email)
    print(existing_user)
    if existing_user:
        raise UserExistException
    hashed_password = get_pass_hash(user_data.password)
    await UsersDAO.add(email = user_data.email,
                       name = user_data.name, 
                       surname = user_data.surname, 
                       hashed_password = hashed_password)
    print(f"пользователь сохранен в бд:{user_data}")
    
@router.post("/login")
async def login_user(response:Response, user_data:UserLogin):
    user = await auth_user(user_data.email, user_data.password)
    access_token = create_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token)
    return {"access_token": access_token}

@router.get("/me")
async def user_get_itself(current_user: UserModel = Depends(get_current_user)) -> User:
    return current_user
    
@router.get("/{id}")
async def get_users_info(id:int) -> User:
    return  await UsersDAO.find_by_id(id)