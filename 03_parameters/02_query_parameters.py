from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 101, "name": "Laptop", "price": 55000},
    {"id": 102, "name": "Keyboard", "price": 1500},
    {"id": 103, "name": "Mouse", "price": 800},
    {"id": 104, "name": "Monitor", "price": 12000},
    {"id": 105, "name": "Webcam", "price": 2500},
]


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Query Parameters Session"}


@app.get("/products")
def get_products(limit: int = 3):
    return products[:limit]


@app.get("/search")
def search_product(name: str):
    filtered_products = []

    for product in products:
        if name.lower() in product["name"].lower():
            filtered_products.append(product)

    return filtered_products