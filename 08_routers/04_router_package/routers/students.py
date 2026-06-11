from fastapi import APIRouter

router = APIRouter()

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


@router.get("/students")
def get_students():
    return {"students": students}
