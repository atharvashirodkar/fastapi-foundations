import json
from fastapi import FastAPI

app = FastAPI()


with open("in_memory_database.json", "r") as file:
    students = json.load(file)


@app.get("/")
def home():
    return {"message": "Delete Student Example"}


@app.get("/students")
def get_students():
    return {"students": students}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            return {"message": "Student deleted successfully", "student": student}

    return {"message": "Student not found"}
