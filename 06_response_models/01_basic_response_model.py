from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str


@app.get("/")
def home():
    return {"message": "Basic Response Model Example"}


@app.get(
    "/student",
    response_model=Student
)
def get_student():
    return {
        "name": "Rahul",
        "age": 22,
        "course": "Python"
    }