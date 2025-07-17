from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.product import Product


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product_by_id(
    session: AsyncSession,
    product_id: int,
) -> Product | None:
    return await session.get(Product, product_id)
