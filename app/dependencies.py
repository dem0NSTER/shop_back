from typing import Annotated

from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_settings import db_settings
from app.schemas.basket_schemas import Basket, CreateBasket
from app.schemas.product_schemas import Product
from app.schemas.user_schemas import User
from app.crud import user_crud
from app.crud import product_crud
from app.crud import basket_crud


async def validate_user(
    user_id: int,
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> None:
    user = await user_crud.get_user_by_id(
        session=session,
        user_id=user_id,
    )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )


async def user_by_id(
    user_id: Annotated[int, Path(gt=0)],
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> User:
    user = await user_crud.get_user_by_id(
        session=session,
        user_id=user_id,
    )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    return user


async def product_by_id(
    product_id: Annotated[int, Path(gt=0)],
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> Product:
    product = await product_crud.get_product_by_id(
        session=session,
        product_id=product_id,
    )
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="product not found"
        )
    return product


async def basket_by_id(
    basket_id: Annotated[int, Path(gt=0)],
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> Basket:
    basket = await basket_crud.get_basket_by_id(
        basket_id=basket_id,
        session=session,
    )
    if basket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="basket not found"
        )
    return basket


async def basket_by_user_id(
    user_id: Annotated[int, Path(gt=0)],
    session: AsyncSession = Depends(db_settings.session_dependency),
) -> Basket:
    basket = await basket_crud.get_basket_by_user_id(
        user_id=user_id,
        session=session,
    )
    if basket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="basket not found"
        )
    return basket
