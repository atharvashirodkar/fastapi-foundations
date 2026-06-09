from fastapi import FastAPI

app = FastAPI()


@app.get(
    "/students",
    tags=["Students"],
    summary="Get all students",
    description="Returns a list of all available students."
)
def get_students():
    return {
        "students": ["Rahul", "Amit", "Priya"]
    }


@app.post(
    "/students",
    tags=["Students"],
    summary="Create a student",
    description="Creates a new student record."
)
def create_student():
    return {
        "message": "Student created successfully"
    }


@app.put(
    "/students",
    tags=["Students"],
    summary="Replace students",
    description="Replaces the existing student collection."
)
def replace_students():
    return {
        "message": "Student list replaced"
    }


@app.delete(
    "/students",
    tags=["Students"],
    summary="Delete a student",
    description="Deletes a student record."
)
def delete_student():
    return {
        "message": "Student deleted successfully"
    }