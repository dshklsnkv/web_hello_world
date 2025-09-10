from web.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime


class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patronymic = Column(String, nullable=True)
    # login = Column(String, nullable=False)
    time_created: Mapped[datetime] = mapped_column(server_default=func.now())
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True, unique=True)
    hashed_password: Mapped[str]
    