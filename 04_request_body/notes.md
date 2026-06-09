# 📝 Request Body Notes

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

## 📦 What is a Request Body?

A request body is data sent by the client to the server.

Unlike path parameters and query parameters, request body data is sent inside the HTTP request.

Example:

```http
POST /students
```

Body:

```json
"Rahul"
```

---

## 🤔 Why Do We Need Request Bodies?

Imagine creating a student.

Using path parameters:

```text
/students/Rahul/22/Python
```

Problems:

- Difficult to read
- Difficult to maintain
- Not suitable for large amounts of data

---

Using query parameters:

```text
/students?name=Rahul&age=22&course=Python
```

This works for small inputs but becomes messy as the data grows.

Example:

```text
/students?name=Rahul&age=22&course=Python&email=rahul@example.com&city=Mumbai
```

---

A request body allows us to send structured data:

```json
{
  "name": "Rahul",
  "age": 22,
  "course": "Python",
  "email": "rahul@example.com",
  "city": "Mumbai"
}
```

This is easier to read, extend, and validate.

## 🧭 Choosing Between Path, Query, and Request Body

### Path Parameters

Used to identify a specific resource.

Example:

```text
/students/101
```

Question being answered:

```text
Which student?
```

---

### Query Parameters

Used to filter or customize results.

Example:

```text
/students?course=Python
```

Question being answered:

```text
How should the results be filtered?
```

---

### Request Body

Used to send data to the server.

Example:

```json
{
  "name": "Rahul",
  "age": 22
}
```

Question being answered:

```text
What data should be created or updated?
```

## 📌 When Are Request Bodies Used?

Request bodies are commonly used when:

- Creating data
- Updating data
- Submitting forms
- Sending structured information

Examples:

```text
Create User
Create Student
Create Product
Update Profile
Place Order
```

---

## 🧾 JSON Request Body

The most common request body format is JSON.

Example:

```json
{
  "name": "Rahul",
  "age": 22,
  "course": "Python"
}
```

FastAPI automatically converts JSON data into Python objects.

---

## 🏗️ JSON Structures

### JSON String

```json
"Rahul"
```

---

### JSON Number

```json
22
```

---

### JSON Array

```json
[
  "Python",
  "FastAPI",
  "SQL"
]
```

---

### JSON Object

```json
{
  "name": "Rahul",
  "age": 22
}
```

---

### Nested JSON Object

```json
{
  "name": "Rahul",
  "address": {
    "city": "Mumbai",
    "state": "Maharashtra"
  }
}
```

## 🔄 JSON to Python Conversion

### JSON String

```json
"Rahul"
```

↓

### Python String

```python
name = "Rahul"
```

---

### JSON Object

```json
{
  "name": "Rahul",
  "age": 22
}
```

↓

### Python Dictionary

```python
{
    "name": "Rahul",
    "age": 22
}
```

---

## 📦 What is Body(...)?

FastAPI uses `Body(...)` to indicate that data should be read from the request body.

Example:

```python
@app.post("/students")
def create_student(name: str = Body(...)):
    return {"name": name}
```

The `...` means:

```text
Required value
```

The client must provide the value in the request body.


## 📖 Swagger and Request Bodies

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger automatically generates:

- Request body examples
- Data types
- API documentation
- Interactive testing tools

You can test request bodies directly from the browser.

---

## ⚠️ The Problem with Dictionaries

In this module we used:

```python
student: dict
```

This means FastAPI accepts any dictionary.

Valid:

```json
{
  "name": "Rahul",
  "age": 22
}
```

Also accepted:

```json
{
  "random": "data"
}
```

Also accepted:

```json
{
  "xyz": 123
}
```

The application has no idea which fields are expected.

As applications grow, this becomes difficult to manage.

---

## 🚀 The Solution: Pydantic Models

Instead of:

```python
student: dict
```

we can define:

```python
class Student(BaseModel):
    name: str
    age: int
```

Now FastAPI knows:

- Which fields are required
- Which data types are expected
- What should be rejected

This is exactly what we'll learn in the next module.

## ✅ Session Summary

In this session, you learned:

- What a request body is
- When request bodies are used
- JSON request bodies
- JSON to Python conversion
- Nested JSON objects
- Swagger request body testing
- Limitations of dictionaries

You are now ready to learn Pydantic models and request validation.