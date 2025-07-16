from app.core.models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User)
    result: Result = await session.execute(stmt)
    res = result.scalars().all()
    return list(res)


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)
