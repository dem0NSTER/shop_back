from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.core.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.core.models.basket import Basket


class User(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(32))
    email: Mapped[str | None]

    basket: Mapped["Basket"] = relationship(back_populates="user")
