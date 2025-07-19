from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from app.crud import basket_crud as crud
from app.schemas.basket_schemas import Basket, CreateBasket
from app.dependencies import validate_user
from app.core.db_settings import db_settings


async def create_basket(
    basket_in: CreateBasket,
    session: AsyncSession,
) -> Basket:
    await validate_user(
        user_id=basket_in.user_id,
        session=session,
    )

    return await crud.create_basket(
        basket_in=basket_in,
        session=session,
    )


async def delete_basket_by_basket_id(
    basket: Basket,
    session: AsyncSession,
) -> None:
    await crud.delete_basket(basket=basket, session=session)


async def delete_basket_by_user_id(
    user_id: int,
    session: AsyncSession,
) -> None:
    await validate_user(
        user_id=user_id,
        session=session,
    )
    await crud.get_basket_by_user_id(
        user_id=user_id,
        session=session,
    )
