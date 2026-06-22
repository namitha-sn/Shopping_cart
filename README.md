Shopping Cart Rest API

Overview

This project is a Shopping Cart REST API built using FastAPI and Pydantic. 
It supports creating and managing shopping carts, adding products, updating quantities, 
and deleting products from a cart.

Technology Stack

Python
FastAPI
Pydantic
Uvicorn

Features

View all carts
View a specific cart
Add products to a cart
Update product quantity
Delete products from a cart
Input validation using Pydantic

API Endpoints

Get All Carts
GET /cart

Get Cart By ID
GET /cart/{cart_id}

Add Item To Cart
POST /cart/{cart_id}/items

Update Item Quantity
PATCH /cart/{cart_id}/items/{product_id}

Delete Item From Cart
DELETE /cart/{cart_id}/items/{product_id}

Sample Request

{
"product_id": "Prod_9942",
"name": "Premium Ski Goggles",
"quantity": 2,
"price": 89.99
}

Run the Application

Install dependencies
pip install fastapi uvicorn

Start the server
uvicorn api --reload

Open Swagger UI
http://127.0.0.1:8000/docs
