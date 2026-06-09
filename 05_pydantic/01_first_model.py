from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str


@app.get("/")
def home():
    return {"message": "First Pydantic Model"}


@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student": student
    }