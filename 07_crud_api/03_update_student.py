import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StudentUpdate(BaseModel):
    name: str
    course: str


with open("in_memory_database.json", "r") as file:
    students = json.load(file)


@app.get("/")
def home():
    return {"message": "Update Student Example"}


@app.get("/students")
def get_students():
    return {"students": students}


@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: StudentUpdate):
    for student in students:
        if student["id"] == student_id:
            student["name"] = updated_student.name
            student["course"] = updated_student.course

            return {"message": "Student updated successfully", "student": student}

    return {"message": "Student not found"}
