from fastapi import APIRouter

router = APIRouter()

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
]


@router.get("/students")
def get_students():
    return {"students": students}


@router.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return {"student": student}
    return {"message":"student not found"}