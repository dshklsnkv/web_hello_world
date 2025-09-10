from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime, date
from phonenumbers import PhoneNumber
from pydantic_extra_types.phone_numbers import PhoneNumber

class RussiaPN(PhoneNumber):
    supported_regions=['RU']
    default_region_code = "+7"

class UserReg(BaseModel):
    email:EmailStr
    # login: str
    name:str
    surname: str
    password: str
    
class UserLogin(BaseModel):
    email:EmailStr
    # login: str
    # name:str
    # surname: str
    password: str
    

class User(BaseModel):
    id: Optional[int] = None
    name:str = "string"
    surname: str = "string"
    patronymic: Optional[str] = None
    # age:int
    # birth_date:date
    # login: str = "string"
    time_created: Optional[datetime]  = None
    email:Optional[EmailStr] = None
    phone_number: Optional[RussiaPN] = None
    
class UserSearch(BaseModel):
    name:str = ""
    surname: str = ""
    patronymic: Optional[str] = None
    # login: str = "string"
    email:Optional[EmailStr] = None
    phone_number: Optional[RussiaPN] = None
    
    # @field_validator("age")
    # @classmethod
    # def validate_age(cls, value):
    #     if value < 18:
    #         raise ValueError("Вам должно быть больше 18 лет!")
    #     elif value > 99:
    #         raise ValueError("Вам должно быть не больше 99 лет")
    #     return value
    
    # @field_validator("login")
    # @classmethod
    # def login_validator(cls, value:str):
    #     return value.lower()
    
    # @field_validator("phone_number", mode="before")
    # @classmethod
    # def phone_validator(cls, value:str):
    #     if value is not None:
    #         if value.startswith("8"):
    #             value = value.replace("8", "+7", 1)
    #         return value
    
    # @field_validator('name', 'surname', 'patronymic')
    # def check_capital_letter(cls, value):
    #     if value is not None and not value.istitle():
    #         raise ValueError('Имя, фамилия и отчество должны начинаться с большой буквы')
    #     return value

    # @field_validator('birth_date')
    # def check_age(cls, value):
    #     today = date.today()
    #     age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    #     if not (18 <= age <= 99):
    #         raise ValueError('Возраст должен быть от 18 до 99 лет')
    #     return value