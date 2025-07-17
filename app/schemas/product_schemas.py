from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(max_length=32)
    description: str | None
    price: int = Field(gt=0)


class Product(ProductBase):
    id: int
