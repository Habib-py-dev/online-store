## GET /products

- Description: Retrieve all products.
- Response: JSON array of products.

## GET /products/{product_id}

- Description: Retrieve a product by ID.
- Response: Product details or 404 if not found.

## POST /products

- Description: Create a new product.
- Request Body:

  {
  "id": int,
  "name": string,
  "price": float,
  "stock": int,
  "category": string
  }

- Response: Created product or 400 if ID exists.

## PUT /products/{product_id}

- Description: Update a product.
- Request Body: Same as POST.
- Response: Updated product or 404 if not found.

## DELETE /products/{product_id}

- Description: Delete a product.
- Response: Success message or 404 if not found.
