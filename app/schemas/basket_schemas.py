from pydantic import BaseModel


class BaseBasket(BaseModel):
    user_id: int


class CreateBasket(BaseBasket):
    pass


class Basket(BaseBasket):
    id: int
