from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import basket_crud as crud
from app.schemas.basket_schemas import Basket, CreateBasket

from app.dependencies import validate_user


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
