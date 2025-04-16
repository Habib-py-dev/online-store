Online Store API
A production-ready RESTful API for managing an online store's product catalog, built with FastAPI.

Features
Full CRUD operations for products (20+ items).
Interactive Swagger/OpenAPI documentation (/docs).
Manual testing with Postman and automated tests with pytest.
Modular architecture with routers, models, and in-memory database.
Cross-platform compatibility (Windows, Linux, macOS).

Installation
Clone the repository:

git clone https://github.com/Habib-py-dev/online-store.git
cd online-store

Set up a virtual environment:

python -m venv venv
.\venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Run the server:

python -m uvicorn app.main:app --reload

Usage
Base URL: http://localhost:8000
Swagger documentation: http://localhost:8000/docs
Example POST request:

{
"id": 22,
"name": "VR Headset",
"price": 399.99,
"stock": 10,
"category": "Electronics"
}

Testing
Swagger: Test endpoints interactively at http://localhost:8000/docs.
Postman: Use the Online Store API Collection for manual testing of all endpoints.
Pytest: Run pytest tests/test_products.py for automated unit tests.

Project Structure

online-store/
├── app/
│ ├── **init**.py
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── routers/
│ │ ├── **init**.py
│ │ ├── products.py
├── docs/
│ ├── api_endpoints.md
│ ├── test_results.txt
├── tests/
│ ├── **init**.py
│ ├── test_products.py
├── .gitignore
├── README.md
├── requirements.txt

License
MIT License
