from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.product_schemas import Product, ProductCreate, ProductUpdate
from app.services import product_service as service
from app.core.db_settings import db_settings

from app import dependencies

router = APIRouter(prefix="/products")


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> list[Product]:
    return await service.get_products(session=session)


@router.get("/{product_id}", response_model=Product)
async def get_product_by_id(
    product: Product = Depends(dependencies.product_by_id),
) -> Product:
    return product


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> Product:
    return await service.create_product(product_in=product_in, session=session)


@router.put("/{product_id}", response_model=Product)
async def update_product(
    product_updated: ProductUpdate,
    product_in: Product = Depends(dependencies.product_by_id),
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> Product:
    return await service.update_product(
        session=session,
        product_in=product_in,
        updated_product=product_updated,
    )


@router.delete(
    "/{product_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def delete_product(
    product_in: Product = Depends(dependencies.product_by_id),
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> None:
    await service.delete_product(
        product_in=product_in,
        session=session,
    )
