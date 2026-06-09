from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI Request Body Session"}


@app.post("/students")
def create_student(name: str = Body()):
    return {
        "message": "Student created successfully",
        "student_name": name
    }