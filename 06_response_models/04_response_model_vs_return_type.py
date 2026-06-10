from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    course: str


@app.get("/")
def home():
    return {"message": "Response Model vs Return Type Example"}


@app.get("/student/response-model", response_model=Student)
def get_student_response_model():
    return {
        "id": 106,
        "name": "Rahul",
        "course": "Python",
        "email": "rahul@example.com",
    }


@app.get("/student/return-type")
def get_student_return_type() -> Student:
    return Student(name="Rahul", course="Python")
