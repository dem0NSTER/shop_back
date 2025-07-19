from app.core.models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from app.schemas.user_schemas import CreateUser, UserUpdate


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).limit(5)
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


async def update_user(
    session: AsyncSession,
    user: User,
    user_updated: UserUpdate,
) -> User:
    for key, value in user_updated.model_dump().items():
        setattr(user, key, value)
    await session.commit()
    return user


async def delete_user(
    user_in: User,
    session: AsyncSession,
) -> None:
    await session.delete(instance=user_in)
    await session.commit()
