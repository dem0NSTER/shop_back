from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import product_crud as crud
from app.schemas.product_schemas import Product, ProductCreate, ProductUpdate


async def get_products(session: AsyncSession) -> list[Product]:
    products = await crud.get_products(session=session)
    return products


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
    product_in: Product,
) -> Product:
    return await crud.update_product(
        updated_product=updated_product,
        product=product_in,
        session=session,
    )


async def delete_product(product_in: Product, session: AsyncSession) -> None:
    await crud.delete_product(
        product_deleted=product_in,
        session=session,
    )
