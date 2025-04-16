# app/models.py
# Pydantic models for data validation and serialization

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    category: str

    class Config:
        # Enable ORM compatibility for future database integration
        from_attributes = True
