
from fastapi import Depends, Request
from jose import jwt, JWTError
from web.exceptions import TokenIncorrect, TokenMissing, UserNotPresent
from web.settings import settings
from web.users.dao import UsersDAO

def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise TokenMissing
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            settings.ALGORITHM
        )
    except JWTError:
        raise TokenIncorrect
    user_id: int = int(payload.get("sub"))
    user = await UsersDAO.find_by_id(user_id)
    if not user:
        raise UserNotPresent
    return user