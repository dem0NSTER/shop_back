from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.product import Product
from app.schemas.product_schemas import ProductCreate


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


async def create_product(
    session: AsyncSession,
    product_in: ProductCreate,
) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    return product
