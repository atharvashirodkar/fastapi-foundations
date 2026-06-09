# 📝 Routes Notes

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

   Replace `filename` with the name of the Python file (without the `.py` extension) that contains the FastAPI `app` instance.

   Example:

   ```bash
   uvicorn main:app --reload
   ```

---

## 🚀 What is a Route?

A route is a URL path that maps to a Python function.

Example:

```python
@app.get("/students")
def get_students():
    return {"message": "Students Route"}
```

Route:

```text
/students
```

When a client visits a route, FastAPI executes the associated function.

---

## 🎯 What is an Endpoint?

An endpoint is a combination of:

```text
HTTP Method + Route Path
```

Examples:

```text
GET /students
POST /students
PUT /students
DELETE /students
```

Although the path is the same, each endpoint performs a different operation.

---

## 🌐 Common HTTP Methods

### GET

Used to retrieve data.

```text
GET /students
```

Example:

```text
Get all students
Get a student by ID
Get all products
```

---

### POST

Used to create new data.

```text
POST /student
```

Example:

```text
Create a student
Create a product
Create a user
```

---

### PUT

Used to replace existing data.

```text
PUT /students
```

Example:

```text
Replace a student's information
Replace a product record
```

---

### PATCH

Used to partially update existing data.

```text
PATCH /student
```

Example:

```text
Update only the student's name
Update only the student's email
```

---

### DELETE

Used to remove data.

```text
DELETE /student
```

Example:

```text
Delete a student
Delete a product
Delete a user
```

---

## 📖 Route Metadata

FastAPI allows additional information to be attached to routes.

These details appear automatically in Swagger UI.

---

### tags

Groups related endpoints together.

```python
tags=["Students"]
```

---

### summary

Short description shown in Swagger UI.

```python
summary="Get all students"
```

---

### description

Detailed explanation shown when an endpoint is expanded.

```python
description="Returns a list of all available students."
```

---

## 🌐 Swagger UI

FastAPI automatically generates interactive API documentation.

URL:

```text
http://127.0.0.1:8000/docs
```

Features:

- View endpoints
- Read documentation
- Execute requests
- Inspect responses

---

## 📬 Postman

Postman is a tool used for API testing.

Benefits:

- Send requests
- Inspect responses
- Save collections
- Organize APIs
- Test APIs without building a frontend

---

## 🔍 Swagger vs Postman

| Swagger UI | Postman |
|------------|----------|
| Built into FastAPI | Separate application |
| Quick API testing | Advanced API testing |
| Auto-generated docs | Collections & environments |
| Good for learning | Common in real projects |

---

## ✅ Session Summary

In this session, you learned:

- What routes are
- What endpoints are
- Common HTTP methods
- Route metadata
- Swagger UI
- Postman basics

You are now ready to work with dynamic routes using path and query parameters.