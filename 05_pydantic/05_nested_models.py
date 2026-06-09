from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Address(BaseModel):
    city: str
    state: str
    pincode: str


class Student(BaseModel):
    name: str
    age: int
    course: str
    address: Address


@app.get("/")
def home():
    return {"message": "Nested Models Example"}


@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student": student
    }