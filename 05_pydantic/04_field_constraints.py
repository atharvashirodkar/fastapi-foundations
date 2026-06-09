from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50
    )
    age: int = Field(
        ge=18,
        le=60
    )


class Product(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=100
    )
    price: float = Field(
        gt=0
    )
    quantity: int = Field(
        ge=1
    )


class User(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=20
    )


@app.get("/")
def home():
    return {"message": "Field Constraints Example"}


@app.post("/students")
def create_student(student: Student):
    return student


@app.post("/products")
def create_product(product: Product):
    return product


@app.post("/users")
def create_user(user: User):
    return user