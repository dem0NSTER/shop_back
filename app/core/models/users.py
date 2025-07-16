from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.core.models.base import Base


class User(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(32))
    email: Mapped[str | None]
