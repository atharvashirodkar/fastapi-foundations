# 📝 Routers Notes

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
   pip install fastapi uvicorn
   ```
   
5. Run the FastAPI application.

   ```bash
   uvicorn main:app --reload
   ```

---

## 🤔 Why Do We Need Routers?

So far, all routes lived in a single file.

Example:

```python
@app.get("/students")
@app.post("/students")
@app.put("/students/{id}")
@app.delete("/students/{id}")
```

For small applications, this is fine.

As applications grow, the file becomes harder to read and maintain.

---

Imagine an API with:

```text
Students
Courses
Products
Users
Orders
Payments
Reports
```

Keeping everything inside:

```text
main.py
```

quickly becomes messy.

---

## 📦 What is APIRouter?

FastAPI provides:

```python
APIRouter
```

to group related endpoints.

Example:

```python
from fastapi import APIRouter

router = APIRouter()
```

Routes can now be moved into separate files.

---

## 🔄 Before and After Routers

### Before

```text
main.py
│
├── Student Routes
├── Course Routes
├── User Routes
└── Product Routes
```

---

### After

```text
main.py

students.py
courses.py
users.py
products.py
```

Each file handles a specific feature.

---

## 🔗 include_router()

Creating a router is not enough.

It must be registered with FastAPI.

Example:

```python
app.include_router(student_router)
```

Without this line, FastAPI will not know about the routes.

---

## 📚 Multiple Routers

A FastAPI application can have multiple routers.

Example:

```python
app.include_router(student_router)
app.include_router(course_router)
app.include_router(product_router)
```

This allows different features to remain independent.

---

## 🏷️ Router Prefixes

Instead of repeating:

```python
@router.get("/students")
@router.post("/students")
@router.put("/students/{id}")
```

we can define:

```python
router = APIRouter(
    prefix="/students"
)
```

and write:

```python
@router.get("/")
@router.post("/")
@router.put("/{id}")
```

FastAPI automatically adds:

```text
/students
```

to every route.

---

## 📖 Generated Routes

Example:

```python
router = APIRouter(
    prefix="/students"
)
```

Route:

```python
@router.get("/")
```

becomes:

```text
/students
```

---

Route:

```python
@router.get("/{student_id}")
```

becomes:

```text
/students/{student_id}
```

---

## 🏷️ Router Tags

Tags organize endpoints inside Swagger UI.

Example:

```python
router = APIRouter(
    prefix="/students",
    tags=["Students"]
)
```

---

Swagger groups endpoints as:

```text
Students
├── GET
├── POST
├── PUT
└── DELETE
```

This makes documentation easier to navigate.

---

## 📦 Router Packages

As projects continue to grow:

```text
main.py
students.py
courses.py
products.py
users.py
orders.py
```

the root folder becomes crowded.

---

A common solution is:

```text
routers/
├── students.py
├── courses.py
├── products.py
└── users.py
```

All routing-related files stay together.

---

## 📄 What is __init__.py?

Example:

```text
routers/
├── __init__.py
├── students.py
└── courses.py
```

The file:

```python
__init__.py
```

marks the folder as a Python package.

This allows imports such as:

```python
from routers.students import router
```

---

## 🌍 Real-World Example

A larger project may look like:

```text
main.py

routers/
├── students.py
├── courses.py
├── products.py
├── users.py
├── orders.py
└── payments.py
```

Each router manages a different part of the API.

---

## 🚀 Benefits of Routers

```text
✓ Better organization
✓ Smaller files
✓ Easier maintenance
✓ Easier teamwork
✓ Cleaner project structure
✓ Better scalability
```

---

## ⚠️ Common Beginner Mistake

Creating routers but forgetting:

```python
app.include_router(...)
```

Result:

```text
404 Not Found
```

because FastAPI never registered the routes.

---

## 🎯 When Should You Create Routers?

A simple rule:

### Small Project

```text
1–5 endpoints
```

Single file is acceptable.

---

### Growing Project

```text
Students
Courses
Products
Users
```

Start using routers.

---

## ✅ Session Summary

In this session, you learned:

- Why routers are needed
- What APIRouter is
- How to create routers
- How to register routers
- Multiple routers
- Router prefixes
- Router tags
- Router packages
- __init__.py
- Common router structures

You can now organize FastAPI applications using routers instead of placing every endpoint in a single file.