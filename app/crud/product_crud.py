from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.product import Product
from app.schemas.product_schemas import ProductCreate, ProductUpdate


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).limit(5)
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


async def update_product(
    updated_product: ProductUpdate,
    product: Product,
    session: AsyncSession,
) -> Product:
    for name, value in updated_product.model_dump().items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
    product_deleted: Product,
    session: AsyncSession,
) -> None:
    await session.delete(product_deleted)
    await session.commit()
