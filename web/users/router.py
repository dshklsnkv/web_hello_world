from datetime import datetime
from fastapi import APIRouter

from users.schema import User

router = APIRouter(prefix="/users", tags=["Users", "Auth"])

@router.get("/{id}")
def get_users_info(id:int) -> User:
    user_data = User(
        name=f"vasya_{id}",
        surname=f"ivanov_{id}",
        patronymic=None,
        login=f"ivanovv_{id}",
        date_reg=datetime(2024, 9, 8, 14, 55)
    )
    return user_data

@router.post("/")
def register_user(user_data: User) -> User:
    print(f"пользователь сохранен в бд:{user_data}")
    print(user_data.login)
    print(user_data.date_reg.year)
    return user_data