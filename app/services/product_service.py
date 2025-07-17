from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import product_crud as crud
from app.schemas.product_schemas import Product


async def get_products(session: AsyncSession) -> list[Product]:
    products = await crud.get_products(session=session)
    return products


async def get_product_by_id(
    session: AsyncSession,
    product_id: int,
) -> Product:
    product = await crud.get_product_by_id(
        session=session,
        product_id=product_id,
    )
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="product not found"
        )
    return product
