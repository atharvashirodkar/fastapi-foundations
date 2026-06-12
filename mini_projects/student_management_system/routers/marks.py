import json

from fastapi import APIRouter
from models.models import Mark, MarkResponse

router = APIRouter(
    prefix="/marks",
    tags=["Marks"]
)

FILE_PATH = "data/marks.json"


def read_data():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def write_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


@router.get("/", response_model=list[MarkResponse])
def get_marks():
    return read_data()


@router.get(
    "/student/{student_id}",
    response_model=list[MarkResponse]
)
def get_student_marks(student_id: int):
    marks = read_data()

    return [
        mark
        for mark in marks
        if mark["student_id"] == student_id
    ]


@router.post("/", response_model=MarkResponse)
def create_mark(mark: Mark):
    marks = read_data()

    new_mark = mark.model_dump()

    marks.append(new_mark)

    write_data(marks)

    return new_mark


@router.put(
    "/{student_id}/{course_id}",
    response_model=MarkResponse
)
def update_mark(
    student_id: int,
    course_id: int,
    updated_mark: Mark
):
    marks = read_data()

    for mark in marks:
        if (
            mark["student_id"] == student_id
            and mark["course_id"] == course_id
        ):
            mark["marks"] = updated_mark.marks

            write_data(marks)

            return mark

    return {"message": "Mark record not found"}


@router.delete("/{student_id}/{course_id}")
def delete_mark(
    student_id: int,
    course_id: int
):
    marks = read_data()

    for mark in marks:
        if (
            mark["student_id"] == student_id
            and mark["course_id"] == course_id
        ):
            marks.remove(mark)

            write_data(marks)

            return {
                "message": "Mark record deleted successfully"
            }

    return {"message": "Mark record not found"}