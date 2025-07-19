from fastapi import APIRouter, Depends, status

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


@router.post("/", response_model=Basket, status_code=status.HTTP_201_CREATED)
async def create_basket(
    basket_in: CreateBasket,
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> Basket:
    return await service.create_basket(
        basket_in=basket_in,
        session=session,
    )


@router.delete(
    "/{basket_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def delete_basket_by_basket_id(
    basket: Basket = Depends(dependencies.basket_by_id),
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> None:
    await service.delete_basket_by_basket_id(basket=basket, session=session)
