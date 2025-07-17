from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import product_crud as crud
from app.schemas.product_schemas import Product, ProductCreate, ProductUpdate


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


async def create_product(
    session: AsyncSession,
    product_in: ProductCreate,
) -> Product:
    product = await crud.create_product(
        session=session,
        product_in=product_in,
    )
    return product


async def update_product(
    session: AsyncSession,
    updated_product: ProductUpdate,
    product_id: int,
) -> Product:
    product = await get_product_by_id(
        session=session,
        product_id=product_id,
    )

    return await crud.update_product(
        updated_product=updated_product,
        product=product,
        session=session,
    )


async def delete_product(product_id: int, session: AsyncSession) -> None:
    product = await get_product_by_id(
        session=session,
        product_id=product_id,
    )
    await crud.delete_product(
        product_deleted=product,
        session=session,
    )
