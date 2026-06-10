# 📝 Response Models Notes

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

## 📦 What is a Response Model?

A response model defines the structure of data sent back to the client.

Example:

```python
class Student(BaseModel):
    name: str
    course: str
```

```python
@app.get(
    "/student",
    response_model=Student
)
```

The response must follow the `Student` model.

---

## 🔄 Request Models vs Response Models

### Request Model

Used for incoming data.

```python
@app.post("/students")
def create_student(student: Student):
```

Question:

```text
What data can the client send?
```

---

### Response Model

Used for outgoing data.

```python
@app.get(
    "/student",
    response_model=Student
)
```

Question:

```text
What data should the client receive?
```

---

## 🎯 Why Use Response Models?

Without a response model:

```python
@app.get("/student")
def get_student():
    return {
        "name": "Rahul",
        "course": "Python",
        "email": "rahul@example.com"
    }
```

FastAPI returns everything.

---

With a response model:

```python
response_model=Student
```

Response:

```json
{
  "name": "Rahul",
  "course": "Python"
}
```

Extra fields are removed automatically.

---

## 🛡️ Response Filtering

Response models can hide data.

Returned data:

```python
{
    "id": 1,
    "name": "Rahul",
    "email": "rahul@example.com",
    "password": "secret123"
}
```

Response model:

```python
class UserResponse(BaseModel):
    id: int
    name: str
```

Client receives:

```json
{
  "id": 1,
  "name": "Rahul"
}
```

Sensitive data stays hidden.

---

## 📋 Response Models for Lists

Single object:

```python
response_model=Student
```

Response:

```json
{
  "name": "Rahul",
  "course": "Python"
}
```

---

Multiple objects:

```python
response_model=list[Student]
```

Response:

```json
[
  {
    "name": "Rahul",
    "course": "Python"
  },
  {
    "name": "Amit",
    "course": "FastAPI"
  }
]
```

Every item is validated individually.

---

## ✅ Response Validation

Response models validate outgoing data.

Example model:

```python
class Student(BaseModel):
    age: int
```

Returned data:

```python
{
    "age": "twenty two"
}
```

Result:

```text
ResponseValidationError
```

because:

```text
Expected: int
Received: str
```

---

## 📖 Swagger Integration

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger automatically displays:

- Response schema
- Data types
- Expected fields
- Example responses

This improves API documentation significantly.

---

## 🔍 response_model vs Return Type Annotation

FastAPI provides two ways to describe the response structure.

### Approach 1: response_model

```python
@app.get(
    "/student",
    response_model=Student
)
def get_student():
    return {
        "name": "Rahul",
        "course": "Python"
    }
```

Here, the response structure is defined in the route decorator.

---

### Approach 2: Return Type Annotation

```python
@app.get("/student")
def get_student() -> Student:
    return Student(
        name="Rahul",
        course="Python"
    )
```

Here, the response structure is defined in the function signature.

---

## ✅ Similarities

Both approaches:

- Use Pydantic models
- Validate response data
- Improve Swagger documentation
- Help catch invalid responses

---

## ⚡ Key Difference

### response_model

The endpoint can return:

```python
dict
list
database record
ORM object
```

Example:

```python
return {
    "name": "Rahul",
    "course": "Python",
    "email": "rahul@example.com"
}
```

FastAPI automatically converts and filters the response according to:

```python
response_model=Student
```

---

### Return Type Annotation

The endpoint typically returns:

```python
Student(...)
```

Example:

```python
return Student(
    name="Rahul",
    course="Python"
)
```

The returned object already matches the expected response structure.

---

## 🌍 Which One Will You See More Often?

In real FastAPI projects, data often comes from:

- Databases
- APIs
- ORM models
- Dictionaries

Because of this, you'll commonly see:

```python
response_model=Student
```

rather than manually creating:

```python
Student(...)
```

for every response.

---

## 📌 Beginner Recommendation

Focus on:

```python
response_model=Student
```

throughout this course.

It works naturally with CRUD APIs and database integrations, which you'll build in upcoming modules.

---

## 🌍 Real-World Examples

### User API

```python
response_model=UserResponse
```

Hide:

```text
password
```

---

### Product API

```python
response_model=ProductResponse
```

Return only product details.

---

### Student API

```python
response_model=StudentResponse
```

Control which student information is exposed.

---

## 🚀 Benefits of Response Models

```text
✓ Validation
✓ Response filtering
✓ Better documentation
✓ Predictable API responses
✓ Improved security
✓ Cleaner code
```

---

## ✅ Session Summary

In this session, you learned:

- What response models are
- Request models vs response models
- Response validation
- Response filtering
- List response models
- Swagger integration
- response_model vs return type

You can now control and validate the data your APIs return to clients.