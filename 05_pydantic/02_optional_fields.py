from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str
    email: Optional[str] = None


@app.get("/")
def home():
    return {"message": "Optional Fields Example"}


@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student": student
    }