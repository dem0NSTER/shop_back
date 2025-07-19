from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result, delete
from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException, status

from app.core.models.basket import Basket
from app.schemas.basket_schemas import CreateBasket


async def get_baskets(
    session: AsyncSession,
) -> list[Basket]:
    stmt = select(Basket).limit(5)
    result: Result = await session.execute(stmt)
    baskets = result.scalars().all()
    return list(baskets)


async def get_basket_by_id(basket_id: int, session: AsyncSession) -> Basket | None:
    return await session.get(Basket, basket_id)


async def get_basket_by_user_id(
    user_id: int,
    session: AsyncSession,
) -> Basket | None:
    stmt = select(Basket).where(
        Basket.user_id == user_id,
    )
    result: Result = await session.execute(stmt)
    basket = result.scalar_one_or_none()
    return basket


async def create_basket(
    basket_in: CreateBasket,
    session: AsyncSession,
) -> Basket:
    try:
        basket = Basket(**basket_in.model_dump())
        session.add(basket)
        await session.commit()
        return basket
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="this user already has basket",
        )


async def delete_basket(
    basket: Basket,
    session: AsyncSession,
) -> None:
    await session.delete(basket)
    await session.commit()


async def delete_basket_by_user_id(
    user_id: int,
    session: AsyncSession,
) -> None:
    stmt = delete(Basket).where(Basket.user_id == user_id)
    await session.execute(stmt)
    await session.commit()
