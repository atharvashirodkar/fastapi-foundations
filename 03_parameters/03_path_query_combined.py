from fastapi import FastAPI

app = FastAPI()

products = {
    101: {"name": "Laptop", "price": 55000, "category": "Electronics"},
    102: {"name": "Keyboard", "price": 1500, "category": "Accessories"},
    103: {"name": "Mouse", "price": 800, "category": "Accessories"},
    104: {"name": "Monitor", "price": 12000, "category": "Electronics"}
}


@app.get("/")
def home():
    return {"message": "Path and Query Parameters"}


@app.get("/products/{product_id}")
def get_product(product_id: int, currency: str = "INR"):
    product = products.get(product_id)

    if not product:
        return {"error": "Product not found"}

    return {
        "product": product,
        "currency": currency
    }


@app.get("/users/{user_id}")
def get_user(user_id: int, details: bool = False):
    response = {
        "user_id": user_id
    }

    if details:
        response["email"] = f"user{user_id}@example.com"
        response["city"] = "Mumbai"

    return response