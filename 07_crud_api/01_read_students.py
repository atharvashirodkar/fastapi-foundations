import json
from fastapi import FastAPI

app = FastAPI()


with open("in_memory_database.json", "r") as file:
    students = json.load(file)


@app.get("/")
def home():
    return {"message": "In-Memory Database Example"}


@app.get("/students")
def get_students():
    return {"students": students}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}
