import json

from fastapi import APIRouter
from models.models import Student, StudentResponse

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

FILE_PATH = "data/students.json"


def read_data():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def write_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


@router.get("/", response_model=list[StudentResponse])
def get_students(age: int | None = None):
    students = read_data()

    if age is not None:
        students = [
            student
            for student in students
            if student["age"] == age
        ]

    return students


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    students = read_data()

    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}


@router.post("/", response_model=StudentResponse)
def create_student(student: Student):
    students = read_data()

    new_student = {
        "id": len(students) + 1,
        **student.model_dump()
    }

    students.append(new_student)

    write_data(students)

    return new_student


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    updated_student: Student
):
    students = read_data()

    for student in students:
        if student["id"] == student_id:
            student["name"] = updated_student.name
            student["age"] = updated_student.age

            write_data(students)

            return student

    return {"message": "Student not found"}


@router.delete("/{student_id}")
def delete_student(student_id: int):
    students = read_data()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            write_data(students)

            return {
                "message": "Student deleted successfully"
            }

    return {"message": "Student not found"}