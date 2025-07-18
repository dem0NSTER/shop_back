from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from app.core.models.basket import Basket


async def get_basket_by_user_id(user_id: int, session: AsyncSession) -> Basket | None:
    stmt = select(Basket).where(Basket.user_id == user_id)
    result: Result = await session.execute(stmt)
    basket = result.scalar_one_or_none()
    return basket


async def create_basket() -> Basket:
    pass


async def delete_basket() -> None:
    pass
