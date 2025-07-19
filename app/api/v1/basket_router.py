from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.services import basket_service as service
from app.core.db_settings import db_settings
from app.schemas.basket_schemas import Basket, CreateBasket
from app import dependencies


router = APIRouter(prefix="/basket")


@router.get("/{basket_id}", response_model=Basket)
async def get_basket_by_id(
    basket: Basket = Depends(dependencies.basket_by_id),
) -> Basket:
    return basket


@router.get("/user/{user_id}", response_model=Basket)
async def get_basket_by_user_id(
    _: None = Depends(dependencies.validate_user),
    basket: Basket = Depends(dependencies.basket_by_user_id),
) -> Basket:
    return basket


@router.post("/", response_model=Basket)
async def create_basket(
    basket_in: CreateBasket,
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> Basket:
    return await service.create_basket(
        basket_in=basket_in,
        session=session,
    )
