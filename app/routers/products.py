# app/routers/products.py
# RESTful endpoints for product management

from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Product
from ..database import products

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=List[Product])
async def get_products():
    return products


@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@router.post("/", response_model=Product, status_code=201)
async def create_product(product: Product):
    for existing_product in products:
        if existing_product.id == product.id:
            raise HTTPException(
                status_code=400, detail="Product ID already exists")
    products.append(product)
    return product


@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/{product_id}", status_code=200)
async def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            products.pop(index)
            return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")
