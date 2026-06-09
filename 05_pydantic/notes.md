# 📝 Pydantic Notes

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

## 🤔 What Problem Does Pydantic Solve?

In the previous module, we used:

```python
student: dict
```

Example request:

```json
{
  "name": "Rahul",
  "age": 22
}
```

FastAPI accepted the data as a dictionary.

However:

```json
{
  "random": "value"
}
```

would also be accepted.

There was no structure and no validation.

The application has no idea:

- Which fields should exist
- Which fields are required
- Which data types are expected

As applications grow, managing dictionaries becomes difficult.

---

## 🚀 What is Pydantic?

Pydantic is a data validation library used by FastAPI.

It allows us to define:

- Expected fields
- Data types
- Validation rules
- Default values

using Python classes.

Example:

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    course: str
```

---

## 🧠 Think of a Pydantic Model as a Blueprint

Example:

```python
class Student(BaseModel):
    name: str
    age: int
    course: str
```

This model acts like a blueprint.

Every incoming request must match this structure.

Valid:

```json
{
  "name": "Rahul",
  "age": 22,
  "course": "Python"
}
```

Invalid:

```json
{
  "name": "Rahul"
}
```

because required fields are missing.

## 📦 Pydantic Model

A class that inherits from:

```python
BaseModel
```

is called a Pydantic model.

Example:

```python
class Student(BaseModel):
    name: str
    age: int
```

---

## ✅ Required Fields

Fields without default values are required.

Example:

```python
class Student(BaseModel):
    name: str
    age: int
```

Valid request:

```json
{
  "name": "Rahul",
  "age": 22
}
```

Invalid request:

```json
{
  "name": "Rahul"
}
```

Reason:

```text
age is missing
```

---

## 🔹 Optional Fields

Optional fields may be omitted.

Example:

```python
from typing import Optional

email: Optional[str] = None
```

Valid:

```json
{
  "name": "Rahul",
  "age": 22
}
```

Valid:

```json
{
  "name": "Rahul",
  "age": 22,
  "email": "rahul@example.com"
}
```

---

## 🔹 Default Values

Default values are used when the client does not provide a value.

Example:

```python
course: str = "Python"
```

Request:

```json
{
  "name": "Rahul",
  "age": 22
}
```

Response:

```json
{
  "name": "Rahul",
  "age": 22,
  "course": "Python"
}
```

---

## 🔄 Type Validation

Pydantic validates data types automatically.

Example:

```python
age: int
```

Valid:

```json
{
  "age": 22
}
```

Invalid:

```json
{
  "age": "twenty two"
}
```

Result:

```text
Validation Error
```
---


## 🔹 Field Constraints

After defining fields and data types, we can also define validation rules.

Pydantic can enforce validation rules.

Example:

```python
from pydantic import Field

name: str = Field(
    min_length=2,
    max_length=50
)
```

Example:

```python
age: int = Field(
    ge=18,
    le=60
)
```

Meaning:

```text
2 <= name length <= 50

18 <= age <= 60
```

---

## 📚 Common Field Constraints

### Strings

```python
Field(min_length=3)
```

```python
Field(max_length=20)
```

---

### Numbers

Greater than:

```python
Field(gt=0)
```

Greater than or equal to:

```python
Field(ge=0)
```

Less than:

```python
Field(lt=100)
```

Less than or equal to:

```python
Field(le=100)
```

---

## 🏗️ Nested Models

Models can contain other models.

Example:

```python
class Address(BaseModel):
    city: str
    state: str


class Student(BaseModel):
    name: str
    address: Address
```

Think of nested models as building larger models from smaller reusable models.

Example:

```text
Student
└── Address
```

This keeps models organized and easier to maintain.

Request:

```json
{
  "name": "Rahul",
  "address": {
    "city": "Mumbai",
    "state": "Maharashtra"
  }
}
```

---

## 📖 Swagger Integration

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically generates:

- Request schemas
- Data types
- Required fields
- Validation rules
- Example request bodies

This is one of FastAPI's biggest advantages.

Notice how Swagger automatically updates when the model changes.

Adding:

```python
email: str
```

to a model immediately updates the request schema shown in Swagger UI.

---

## 🌍 Why Pydantic is Important

Benefits:

- Structured data
- Automatic validation
- Better documentation
- Cleaner code
- Easier maintenance

Without Pydantic:

```python
student: dict
```

With Pydantic:

```python
student: Student
```

The code becomes easier to understand and safer to use.

---

## ✅ Session Summary


In this session, you learned:

- What Pydantic is
- Why Pydantic is needed
- Pydantic models
- Required fields
- Optional fields
- Default values
- Field constraints
- Nested models
- Automatic validation
- Swagger integration

You are now ready to control how API responses are returned using Response Models.