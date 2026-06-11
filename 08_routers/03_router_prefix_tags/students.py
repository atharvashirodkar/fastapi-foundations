from fastapi import APIRouter

# tags are optional 
router = APIRouter(prefix="/students", tags=["Students"])

students = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Priya"},
    {"id": 3, "name": "Amit"},
    {"id": 4, "name": "Sneha"},
    {"id": 5, "name": "Vikram"},
    {"id": 6, "name": "Neha"},
    {"id": 7, "name": "Arjun"},
    {"id": 8, "name": "Kavya"},
    {"id": 9, "name": "Rohan"},
    {"id": 10, "name": "Ananya"},
]


@router.get("/")
def get_students():
    return {"students": students}


@router.get("/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return {"student": student}
    return {"message": "student not found"}
