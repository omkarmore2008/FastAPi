from pydantic import BaseModel, EmailStr
from enum import Enum

class UserDetails(BaseModel):
    email: EmailStr
    password: str


class CommonResponseModel(BaseModel):
    status: int
    message: str


class Category(str, Enum):
    smartphones = "smartphones"
    laptops = "laptops"
    fragrances = "fragrances"  
    skincare = "skincare"  
    groceries = "groceries"  
    homedecoration = "home-decoration" 


class RequestModel(BaseModel):
    title: str
    description: str
    price: float
    discountPercentage: float
    rating: float
    stock: int
    brand: str
    category: Category 
    thumbnail: str
    images: list = []
