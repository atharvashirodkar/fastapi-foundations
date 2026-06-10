# 📝 CRUD API Notes

## Running the Examples

Before running any examples in this module:

1. Open this module's folder in the terminal.
2. Create a virtual environment.

   **Windows (PowerShell)**

   ```powershell
   python -m venv venv
   ```

   **Linux / macOS**

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment.

   **Windows (PowerShell)**

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **Linux / macOS**

   ```bash
   source venv/bin/activate
   ```

4. Install the required packages.

   ```bash
   pip install -r requirements.txt
   ```

5. Run the FastAPI application.

   ```bash
   uvicorn filename:app --reload
   ```

---

## 📚 What is CRUD?

CRUD represents the four most common operations performed on data.

```text
C → Create
R → Read
U → Update
D → Delete
```

Almost every backend application performs these operations.

Examples:

- Student Management System
- Product Management System
- User Management System
- Task Manager
- Inventory System

---

## 🧠 CRUD in Real Life

Imagine a student management system.

### Create

Add a new student.

```text
POST /students
```

---

### Read

View student information.

```text
GET /students
```

```text
GET /students/1
```

---

### Update

Modify student information.

```text
PUT /students/1
```

---

### Delete

Remove a student.

```text
DELETE /students/1
```

---

## 🔗 CRUD and HTTP Methods

| CRUD Operation | HTTP Method |
| -------------- | ----------- |
| Create         | POST        |
| Read           | GET         |
| Update         | PUT         |
| Delete         | DELETE      |

---

## 📦 In-Memory Database

In this module, we are not using a real database.

Instead, we store data inside:

```text
in_memory_database.json
```

Example:

```json
[
    {
        "id": 1,
        "name": "Rahul",
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Priya",
        "course": "FastAPI"
    },
    {
        "id": 3,
        "name": "Amit",
        "course": "Django"
    },
    {
        "id": 4,
        "name": "Neha",
        "course": "Data Science"
    },
    .
    .
    .
]
```

The JSON file acts as our temporary data source.

---

## 📖 Loading JSON Data

Example:

```python
import json

with open("in_memory_database.json", "r") as file:
    students = json.load(file)
```

This converts:

```json
[
  {
    "id": 1,
    "name": "Rahul"
  }
]
```

into:

```python
[
    {
        "id": 1,
        "name": "Rahul"
    }
]
```

which can be used by our FastAPI application.

---

## 📌 Why Use a JSON File?

Benefits:

- Avoid repeating data in every file
- More realistic than hardcoded lists
- Reuses Python knowledge
- Easier to maintain

Instead of:

```python
students = [...]
```

inside every file, we keep the data in one place.

---

## ➕ Create Operation

Create adds new data.

Example:

```http
POST /students
```

Request Body:

```json
{
  "name": "Amit",
  "course": "SQL"
}
```

Result:

```json
{
  "id": 3,
  "name": "Amit",
  "course": "SQL"
}
```

---

## 📖 Read Operation

Read retrieves existing data.

Examples:

```http
GET /students
```

```http
GET /students/1
```

Read operations do not modify data.

---

## ✏️ Update Operation

Update modifies existing data.

Example:

```http
PUT /students/1
```

Request Body:

```json
{
  "name": "Rahul Sharma",
  "course": "FastAPI"
}
```

Result:

```json
{
  "id": 1,
  "name": "Rahul Sharma",
  "course": "FastAPI"
}
```

---

## ❌ Delete Operation

Delete removes data.

Example:

```http
DELETE /students/2
```

Result:

```json
{
  "message": "Student deleted successfully"
}
```

---

## 🔄 Typical CRUD Workflow

A common testing sequence:

```text
1. GET    /students

2. POST   /students

3. GET    /students

4. PUT    /students/1

5. GET    /students

6. DELETE /students/2

7. GET    /students
```

This helps visualize how data changes over time.

---

## ⚠️ Limitation of This Approach

The JSON file is only being read.

Our examples do not permanently save changes back to:

```text
in_memory_database.json
```

For example:

```text
POST /students
```

adds a student only while the application is running.

Restarting the server restores the original data.

---

## 🚀 Why Learn CRUD Before Databases?

CRUD teaches:

- API design
- HTTP methods
- Request bodies
- Path parameters
- Data manipulation

without introducing database complexity.

Once CRUD concepts are understood, learning databases becomes much easier.

---

## 🌍 Real-World Examples

### Student API

```text
Create Student
Read Student
Update Student
Delete Student
```

---

### Product API

```text
Create Product
Read Product
Update Product
Delete Product
```

---

### Task Manager API

```text
Create Task
Read Task
Update Task
Delete Task
```

---

## ✅ Session Summary

In this session, you learned:

- What CRUD means
- CRUD and HTTP methods
- Reading data from JSON
- Create operations
- Read operations
- Update operations
- Delete operations
- Typical CRUD workflows
- Limitations of in-memory data

You can now build complete APIs that manage data using CRUD operations.