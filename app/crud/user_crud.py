from app.core.models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from app.schemas.user_schemas import CreateUser


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User)
    result: Result = await session.execute(stmt)
    res = result.scalars().all()
    return list(res)


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def create_user(
    session: AsyncSession,
    user_in: CreateUser,
) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user
