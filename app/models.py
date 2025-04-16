"""Data models for the Online Store API.

Defines Pydantic models for product data validation and serialization.
"""

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
    from_attributes = True
