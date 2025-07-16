from pydantic import BaseModel, Field, EmailStr


class BaseUser(BaseModel):
    username: str = Field(max_length=32)
    email: EmailStr


class CreateUser(BaseUser):
    pass


class User(BaseUser):
    id: int


class UserUpdate(BaseUser):
    pass
