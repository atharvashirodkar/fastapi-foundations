from fastapi import FastAPI
from students import router as students_router
from courses import router as courses_router

app = FastAPI()

app.include_router(students_router)
app.include_router(courses_router)
