from app.core.config import setting
from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)


class DataBaseSettings:
    def __init__(self, db_url: str):
        self.engine = create_async_engine(url=db_url)
        self.__session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def __get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.__session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        session = self.__get_scoped_session()
        async with session() as sess:
            yield sess
            await session.remove()


db_settings = DataBaseSettings(db_url=setting.db_url)
