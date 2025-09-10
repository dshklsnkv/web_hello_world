from passlib.context import CryptContext
from pydantic import EmailStr

from web.exceptions import IncorrectEmailPassword
from web.users.dao import UsersDAO
from jose import jwt
from web.settings import settings
from datetime import datetime, timedelta


pwd_context = CryptContext(schemes=["md5_crypt"], deprecated ="auto")

def get_pass_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_pass(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

async def auth_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one(email=email)
    if not (user and verify_pass(password, user.hashed_password)): 
        raise IncorrectEmailPassword
    return user

def create_token(data:dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=20)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt
    

if __name__=="__main__":
    ...
    # h = get_pass_hash("Start123")
    # verify = verify_pass("Start1234", h)
    # print(verify)
    # from asyncio import run
    # run(auth_user("antoxa@example.com","Anton1234"))