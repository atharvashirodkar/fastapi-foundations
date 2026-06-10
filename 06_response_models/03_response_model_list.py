from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    course: str


@app.get("/")
def home():
    return {"message": "Response Model List example"}


@app.get("/students", response_model=list[Student])
def get_student():
    return [
        {"name": "Sakshi", "course": "SQL", "age": 23, "city": "Mumbai"},
        {"name": "Rahul", "course": "Python", "age": 24, "city": "Pune"},
        {"name": "Sameer", "course": "FastAPI", "age": 27, "city": "Banglore"},
    ]
