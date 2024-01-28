from datetime import datetime
from pydantic import BaseModel, Field


class UserIn(BaseModel):
    name: str = Field(..., title="Name", max_length=32)
    surname: str = Field(None, title="Surname", max_length=32)
    email: str = Field(..., title="Email", max_length=128)
    password: str = Field(..., title="Password", min_length=4, max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(..., title="Name", max_length=32)
    surname: str = Field(None, title="Surname", max_length=32)
    email: str = Field(..., title="Email", max_length=128)
    password: str = Field(..., title="Password", min_length=4, max_length=128)


class ProductIn(BaseModel):
    title: str = Field(..., title="Title", max_length=50)
    description: str = Field(None, title="Description", max_length=500)
    price: int = Field(..., title="Price", gt=0, le=100000)


class Product(BaseModel):
    id: int
    title: str = Field(..., title="Title", max_length=50)
    description: str = Field(None, title="Description", max_length=500)
    price: int = Field(..., title="Price", gt=0, le=100000)


class OrderIn(BaseModel):
    user_id: int
    prod_id: int
    date: datetime = Field(default=datetime.now())
    status: str = Field(default="created")


class Order(BaseModel):
    id: int
    user_id: int
    prod_id: int
    date: str
    status: str = Field(default="created")
