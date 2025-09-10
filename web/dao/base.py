from sqlalchemy import select, insert, delete
from sqlalchemy.orm.exc import MultipleResultsFound

from web.database import async_session_maker

class BaseDAO:
    model = None
    
    @classmethod
    async def find_by_id(cls, model_id:int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalars().one_or_none()
        
    @classmethod
    async def find_one(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().one_or_none()
        
    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
            
    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def delete(cls, model_id: int) -> None:
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.id == model_id)
            await session.execute(query)
            await session.commit()
        
    # async def find(cls, **filter_by):
    #     async with async_session_maker() as session:
    #         query = select(cls.model).filter_by(**filter_by)
    #         try:  
    #             result = await session.execute(query)
    #             return result.scalars().one_or_none()
    #         except MultipleResultsFound as e:
    #             result = await session.execute(query)
    #             return result.scalars().all()