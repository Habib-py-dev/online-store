"""
This module does [describe its purpose].
"""
from typing import ClassVar
from pydantic import BaseModel


class Product(BaseModel):
    """Model for a product in the online store."""
    id: int
    name: str
    price: float
    stock: int
    category: str

    class Config:
        """Configuration for Pydantic model to enable ORM compatibility."""
        from_attributes: ClassVar[bool] = True
