from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., ge=1)


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int


class Course(BaseModel):
    name: str = Field(..., min_length=2)


class CourseResponse(BaseModel):
    id: int
    name: str


class Mark(BaseModel):
    student_id: int
    course_id: int
    marks: int = Field(..., ge=0, le=100)


class MarkResponse(BaseModel):
    student_id: int
    course_id: int
    marks: int
