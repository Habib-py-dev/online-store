# app/database.py
# Simulated in-memory database for product catalog

from typing import List
from .models import Product

# Initial product catalog (replace with SQLAlchemy/PostgreSQL in production)
products: List[Product] = [
    Product(id=1, name="Laptop Pro", price=1299.99,
            stock=15, category="Electronics"),
    Product(id=2, name="Smartphone X", price=699.99,
            stock=25, category="Electronics"),
    Product(id=3, name="Wireless Headphones", price=99.99,
            stock=50, category="Accessories"),
    Product(id=4, name="Gaming Mouse", price=49.99,
            stock=100, category="Accessories"),
    Product(id=5, name="4K Monitor", price=399.99,
            stock=10, category="Electronics"),
    Product(id=6, name="Mechanical Keyboard", price=89.99,
            stock=30, category="Accessories"),
    Product(id=7, name="Smart Watch", price=199.99,
            stock=20, category="Wearables"),
    Product(id=8, name="Tablet Air", price=299.99,
            stock=12, category="Electronics"),
    Product(id=9, name="USB-C Cable", price=19.99,
            stock=200, category="Accessories"),
    Product(id=10, name="Portable Charger", price=39.99,
            stock=60, category="Accessories"),
    Product(id=11, name="Bluetooth Speaker", price=79.99,
            stock=40, category="Accessories"),
    Product(id=12, name="Webcam HD", price=59.99,
            stock=25, category="Accessories"),
    Product(id=13, name="Smart TV", price=599.99,
            stock=10, category="Electronics"),
    Product(id=14, name="Wireless Router", price=129.99,
            stock=15, category="Networking"),
    Product(id=15, name="External SSD", price=149.99,
            stock=20, category="Storage"),
    Product(id=16, name="Gaming Console", price=499.99,
            stock=8, category="Electronics"),
    Product(id=17, name="Fitness Tracker", price=129.99,
            stock=30, category="Wearables"),
    Product(id=18, name="Drone Camera", price=799.99,
            stock=5, category="Electronics"),
    Product(id=19, name="Smart Light Bulb", price=29.99,
            stock=100, category="Smart Home"),
    Product(id=20, name="Electric Kettle", price=49.99,
            stock=50, category="Appliances")
]
