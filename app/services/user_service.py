from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.crud import user_crud as crud
from app.schemas.user_schemas import CreateUser, User, UserUpdate


async def get_users(session: AsyncSession) -> list[User]:
    users = await crud.get_users(session=session)
    return users


async def create_user(
    user_in: CreateUser,
    session: AsyncSession,
) -> User:
    user = await crud.create_user(
        user_in=user_in,
        session=session,
    )
    return user


async def update_product(
    user_in: User,
    user_updated: UserUpdate,
    session: AsyncSession,
) -> User:
    updated_user = await crud.update_user(
        session=session,
        user=user_in,
        user_updated=user_updated,
    )
    return updated_user


async def delete_user(
    user_in: User,
    session: AsyncSession,
) -> None:
    return await crud.delete_user(
        user_in=user_in,
        session=session,
    )
