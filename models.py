from pydantic import BaseModel
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
