from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.product_schemas import Product
from app.services import product_service as service
from app.core.db_settings import db_settings


router = APIRouter(prefix="/products")


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> list[Product]:
    return await service.get_products(session=session)


@router.get("/{product_id}", response_model=Product)
async def get_product_by_id(
    product_id: int,
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> Product:
    return await service.get_product_by_id(session=session, product_id=product_id)
