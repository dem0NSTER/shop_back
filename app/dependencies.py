from typing import Annotated

from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_settings import db_settings
from app.schemas.user_schemas import User
from app.crud import user_crud


async def user_by_id(
    user_id: Annotated[int, Path(gt=0)],
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> User:
    user = await user_crud.get_user_by_id(
        session=session,
        user_id=user_id,
    )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    return user
