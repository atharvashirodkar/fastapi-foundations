import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    course: str


with open("in_memory_database.json", "r") as file:
    students = json.load(file)


@app.get("/")
def home():
    return {"message": "Create Student Example"}


@app.get("/students")
def get_students():
    return {"students": students}


@app.post("/students")
def create_student(student: Student):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "course": student.course,
    }

    students.append(new_student)

    return {"message": "Student created successfully", "student": new_student}
