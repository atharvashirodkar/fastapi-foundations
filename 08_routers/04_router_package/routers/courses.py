from fastapi import APIRouter

router = APIRouter()

courses = [
    {"id": 1, "name": "Python"},
    {"id": 2, "name": "FastAPI"},
    {"id": 3, "name": "JavaScript"},
    {"id": 4, "name": "React"},
    {"id": 5, "name": "SQL"},
    {"id": 6, "name": "Docker"},
    {"id": 7, "name": "Machine Learning"},
    {"id": 8, "name": "Data Structures"},
]


@router.get("/courses")
def get_courses():
    return {"courses": courses}
