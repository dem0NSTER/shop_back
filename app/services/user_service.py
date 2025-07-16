from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.crud import user_crud as crud
from app.schemas.user_schemas import User


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
