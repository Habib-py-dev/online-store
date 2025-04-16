# app/main.py
# Main FastAPI application for Online Store API

from fastapi import FastAPI
from .routers import products

app = FastAPI(
    title="Online Store API",
    description="A scalable RESTful API for managing an online store's product catalog",
    version="1.0.0",
    contact={"name": "Your Name", "email": "your.email@example.com"},
    license_info={"name": "MIT License",
                  "url": "https://opensource.org/licenses/MIT"}
)

app.include_router(products.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Online Store API"}
