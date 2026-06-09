from fastapi import FastAPI

app = FastAPI()

users = {
    1: {"name": "Rahul", "city": "Mumbai"},
    2: {"name": "Amit", "city": "Pune"},
    3: {"name": "Priya", "city": "Delhi"}
}

products = {
    101: {"name": "Laptop", "price": 55000},
    102: {"name": "Keyboard", "price": 1500},
    103: {"name": "Mouse", "price": 800}
}

students = {
    "rahul": {"course": "Python"},
    "amit": {"course": "Java"},
    "priya": {"course": "FastAPI"}
}


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Parameters Session"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users.get(
        user_id,
        {"error": "User not found"}
    )


@app.get("/products/{product_id}")
def get_product(product_id: int):
    return products.get(
        product_id,
        {"error": "Product not found"}
    )


@app.get("/students/{student_name}")
def get_student(student_name: str):
    return students.get(
        student_name.lower(),
        {"error": "Student not found"}
    )