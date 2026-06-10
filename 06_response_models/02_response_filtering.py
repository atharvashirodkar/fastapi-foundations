from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StudentResponse(BaseModel):
    name: str
    course: str


@app.get("/")
def home():
    return {"message": "Response Filtering Example"}


@app.get("/student", response_model=StudentResponse)
def get_student():
    return {
        "name": "Rahul",
        "age": 22,
        "course": "Python",
        "email": "rahul@example.com",
        "phone": "9876543210",
    }
