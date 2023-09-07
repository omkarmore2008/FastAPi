from pydantic import BaseModel, EmailStr
from typing import Union
from enum import Enum


class Predeined(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name : str
    price : float
    is_offer : Union [bool, None] = None


class UserDetails(BaseModel):
    email: EmailStr
    password: str


class CommonResponseModel(BaseModel):
    status: str
    message: str