from app.core.db_settings import db_settings
from app.schemas.user_schemas import CreateUser, User, UserUpdate

from fastapi import APIRouter, Depends, status
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


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: CreateUser,
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> User:
    return await service.create_user(
        user_in=user_in,
        session=session,
    )


@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user_updated: UserUpdate,
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> User:
    return await service.update_product(
        user_id=user_id, user_updated=user_updated, session=session
    )


@router.delete(
    "/{user_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
    user_id: int,
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> None:
    return await service.delete_user(
        user_id=user_id,
        session=session,
    )
