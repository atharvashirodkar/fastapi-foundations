import json

from fastapi import APIRouter
from models.models import Course, CourseResponse

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

FILE_PATH = "data/courses.json"


def read_data():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def write_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


@router.get("/", response_model=list[CourseResponse])
def get_courses(name: str | None = None):
    courses = read_data()

    if name:
        courses = [
            course
            for course in courses
            if name.lower() in course["name"].lower()
        ]

    return courses


@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int):
    courses = read_data()

    for course in courses:
        if course["id"] == course_id:
            return course

    return {"message": "Course not found"}


@router.post("/", response_model=CourseResponse)
def create_course(course: Course):
    courses = read_data()

    new_course = {
        "id": len(courses) + 1,
        **course.model_dump()
    }

    courses.append(new_course)

    write_data(courses)

    return new_course


@router.put("/{course_id}", response_model=CourseResponse)
def update_course(
    course_id: int,
    updated_course: Course
):
    courses = read_data()

    for course in courses:
        if course["id"] == course_id:
            course["name"] = updated_course.name

            write_data(courses)

            return course

    return {"message": "Course not found"}


@router.delete("/{course_id}")
def delete_course(course_id: int):
    courses = read_data()

    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)

            write_data(courses)

            return {
                "message": "Course deleted successfully"
            }

    return {"message": "Course not found"}