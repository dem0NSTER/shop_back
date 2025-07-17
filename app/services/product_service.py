from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import product_crud as crud
from app.schemas.product_schemas import Product


async def get_products(session: AsyncSession) -> list[Product]:
    products = await crud.get_products(session=session)
    return products
