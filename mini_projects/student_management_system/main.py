from fastapi import FastAPI

from routers.students import router as student_router
from routers.courses import router as course_router
from routers.marks import router as marks_router

app = FastAPI(title="Student Management System")

app.include_router(student_router)
app.include_router(course_router)
app.include_router(marks_router)