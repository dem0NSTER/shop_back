from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text

from app.core.models import Base


class Product(Base):
    __tablename__ = "products"
    name: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(
        Text,
        server_default="",
        default="",
    )
    price: Mapped[int]
