from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str = "Python"


@app.get("/")
def home():
    return {"message": "Default Values Example"}


@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student": student
    }