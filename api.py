from fastapi import FastAPI
from pydantic import BaseModel,Field
from fastapi import HTTPException


app=FastAPI()

#Validation using pydantic
class Item(BaseModel):
    product_id: str
    name: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
class UpdateQuantity(BaseModel):
    quantity:int=Field(gt=0)
 
carts={}

#used to get all the cart details(GET METHOD)
@app.get('/cart')
def get_all_carts():
    return carts

#used to get all the cart details for specific ID(GET METHOD)
@app.get('/cart/{cart_id}')
def cart_details(cart_id: int,status_code=200):

    if cart_id not in carts:
        return {}
    return carts[cart_id]

#Add the items to cart(POST METHOD)
@app.post('/cart/{cart_id}/items')
def add_cart_item(cart_id:int,item:Item,status_code=201):
    if cart_id not in carts:
        carts[cart_id]={
                "cart_id":cart_id,
                "items":[],
                "total_items":0,
                "total_price":0.0
            }
    carts[cart_id]["items"].append(item.model_dump())
    carts[cart_id]["total_items"] = sum(
        item["quantity"] for item in carts[cart_id]["items"]
    )

    carts[cart_id]["total_price"] = sum(
        item["quantity"] * item["price"]
        for item in carts[cart_id]["items"]
    )
    return carts[cart_id]

#Used to modify the products quantity(PATCH METHOD)
@app.patch('/cart/{cart_id}/items/{product_id}')
def modift_cart(cart_id:int,product_id: str, update:UpdateQuantity,status_code=200):
    if cart_id not in carts:
        raise HTTPException(status_code=404, detail="Cart not found")

    for item in carts[cart_id]["items"]:
        if item["product_id"] == product_id:
            item["quantity"] = update.quantity

            carts[cart_id]["total_items"] = sum(
                q["quantity"] for q in carts[cart_id]["items"]
            )

            carts[cart_id]["total_price"] = sum(
                p["quantity"] * p["price"]
                for p in carts[cart_id]["items"]
            )

            return carts[cart_id]

    raise HTTPException(status_code=404, detail="Product not found")

# Delete the product item from specific cart_id(DELETE METHOD)
@app.delete('/cart/{cart_id}/items/{product_id}')
def delete_product(cart_id:int,product_id:str,status_code=200):
     if cart_id not in carts:
        return {"message": "Cart not found"}

     items = carts[cart_id]["items"]

     for item in items:
        if item["product_id"] == product_id:
            items.remove(item)
            carts[cart_id]["total_items"] = sum(
                q["quantity"] for q in items
            )
            carts[cart_id]["total_price"] = sum(
                p["quantity"] * p["price"]
                for p in items
            )
            return carts[cart_id]
     raise HTTPException(status_code=404, detail="product not found")