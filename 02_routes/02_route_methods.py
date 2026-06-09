from fastapi import FastAPI, Body

app = FastAPI()

students = ["Rahul", "Amit", "Priya"]


# GET -> Read data
@app.get("/students")
def get_students():
    return {"students": students}


# POST -> Create data
@app.post("/student")
def create_student(name: str = Body(...)):
    students.append(name)

    return {
        "message": "Student added successfully",
        "students": students
    }


# PUT -> Replace entire collection
@app.put("/students")
def replace_students(new_students: list[str] = Body(...)):
    global students

    students = new_students

    return {
        "message": "Student list replaced",
        "students": students
    }


# PATCH -> Modify existing data
@app.patch("/student")
def update_student(
    old_name: str = Body(...),
    new_name: str = Body(...)
):
    if old_name in students:
        index = students.index(old_name)
        students[index] = new_name

        return {
            "message": "Student updated",
            "students": students
        }

    return {
        "message": "Student not found"
    }


# DELETE -> Remove data
@app.delete("/student")
def delete_student(name: str = Body(...)):
    if name in students:
        students.remove(name)

        return {
            "message": f"{name} removed",
            "students": students
        }

    return {
        "message": "Student not found"
    }