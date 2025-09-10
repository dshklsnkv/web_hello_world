from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from web.settings import settings
from sqlalchemy.orm import DeclarativeBase


engine = create_async_engine(settings.database_url)

async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass