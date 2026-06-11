from fastapi import FastAPI
from routers.courses import router as courses_router
from routers.students import router as students_router

app = FastAPI()

app.include_router(students_router)
app.include_router(courses_router)