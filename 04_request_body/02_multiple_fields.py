from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Multiple Fields Request Body"}


# Receive multiple values as a JSON object
@app.post("/students")
def create_student(student: dict = Body(...)):
    return {
        "message": "Student created successfully",
        "student": student
    }