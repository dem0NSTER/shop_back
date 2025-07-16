from app.core.db_settings import db_settings
from app.schemas.user_schemas import User

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import user_service as service

router = APIRouter(prefix="/users")


@router.get("/", response_model=list[User])
async def get_users(
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> list[User]:
    return await service.get_users(
        session=session,
    )


@router.get("/{user_id}", response_model=User)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> User:
    return await service.get_user_by_id(
        user_id=user_id,
        session=session,
    )
