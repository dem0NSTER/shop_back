from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.crud import user_crud as crud
from app.schemas.user_schemas import CreateUser, User, UserUpdate


async def get_users(session: AsyncSession) -> list[User]:
    users = await crud.get_users(session=session)
    return users


async def get_user_by_id(session: AsyncSession, user_id: int) -> User:
    user = await crud.get_user_by_id(
        session=session,
        user_id=user_id,
    )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found",
        )
    return user


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
    user_id: int,
    user_updated: UserUpdate,
    session: AsyncSession,
) -> User:
    user = await get_user_by_id(
        session=session,
        user_id=user_id,
    )
    updated_user = await crud.update_user(
        session=session,
        user=user,
        user_updated=user_updated,
    )
    return updated_user


async def delete_user(
    user_id: int,
    session: AsyncSession,
) -> None:
    user = await get_user_by_id(
        session=session,
        user_id=user_id,
    )

    return await crud.delete_user(
        user_in=user,
        session=session,
    )
