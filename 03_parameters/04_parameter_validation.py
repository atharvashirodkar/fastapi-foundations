from fastapi import FastAPI, Query

app = FastAPI()

products = [
    {"id": 101, "name": "Laptop"},
    {"id": 102, "name": "Keyboard"},
    {"id": 103, "name": "Mouse"},
    {"id": 104, "name": "Monitor"},
    {"id": 105, "name": "Webcam"},
]


@app.get("/")
def home():
    return {"message": "Parameter Validation Example"}


@app.get("/products")
def get_products(
    limit: int = Query(
        default=5,
        ge=1,
        le=10,
        description="Number of products to return"
    )
):
    return products[:limit]


@app.get("/search")
def search_product(
    keyword: str = Query(
        min_length=3,
        max_length=20,
        description="Product name to search"
    )
):
    filtered_products = []

    for product in products:
        if keyword.lower() in product["name"].lower():
            filtered_products.append(product)

    return filtered_products