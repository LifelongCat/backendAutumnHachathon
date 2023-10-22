from abc import ABC, abstractmethod
from sqlalchemy import insert, select

from db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def get_one(self, elem_id):
        raise NotImplementedError

    @abstractmethod
    async def create_one(self, data):
        raise NotImplementedError

    @abstractmethod
    async def check_count(self, elem_id):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get_one(self, elem_id: str):
        async with async_session_maker() as session:
            query = select(self.model).where(self.model.id == elem_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def create_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data)
            await session.execute(stmt)
            await session.commit()
            return data['id']

    async def check_count(self, elem_id: str) -> int:
        async with async_session_maker() as session:
            query = select(self.model).where(self.model.id.contains(elem_id))
            result = await session.execute(query)
            return len(result.all())
