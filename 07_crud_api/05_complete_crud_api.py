from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    course: str


students = [
    {"id": 1, "name": "Rahul", "course": "Python"},
    {"id": 2, "name": "Priya", "course": "FastAPI"},
    {"id": 3, "name": "Amit", "course": "Django"},
    {"id": 4, "name": "Neha", "course": "Data Science"},
    {"id": 5, "name": "Arjun", "course": "Machine Learning"},
    {"id": 6, "name": "Sneha", "course": "Java"},
    {"id": 7, "name": "Vikram", "course": "Spring Boot"},
    {"id": 8, "name": "Ananya", "course": "React"},
    {"id": 9, "name": "Karan", "course": "Node.js"},
    {"id": 10, "name": "Meera", "course": "MongoDB"},
    {"id": 11, "name": "Rohit", "course": "DevOps"},
    {"id": 12, "name": "Pooja", "course": "AWS"},
    {"id": 13, "name": "Sanjay", "course": "Docker"},
    {"id": 14, "name": "Kavya", "course": "Kubernetes"},
    {"id": 15, "name": "Nikhil", "course": "Cyber Security"},
]


@app.get("/")
def home():
    return {"message": "Complete CRUD API Example"}


# Read all students
@app.get("/students")
def get_students():
    return {"students": students}


# Read one student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}


# Create a student
@app.post("/students")
def create_student(student: Student):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "course": student.course,
    }

    students.append(new_student)

    return {"message": "Student created successfully", "student": new_student}


# Update a student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for student in students:
        if student["id"] == student_id:
            student["name"] = updated_student.name
            student["course"] = updated_student.course

            return {"message": "Student updated successfully", "student": student}

    return {"message": "Student not found"}


# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            return {"message": "Student deleted successfully", "student": student}

    return {"message": "Student not found"}
