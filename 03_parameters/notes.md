# 📝 Parameters Notes

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

## 🚀 What Are Parameters?

Parameters allow APIs to receive values from clients.

These values can be used to:

- Identify resources
- Filter data
- Search data
- Customize responses

Example:

```text
/users/101
```

```text
/products?limit=5
```

---

## 📍 Path Parameters

Path parameters are dynamic values embedded directly in the URL path.

Example:

```text
/users/101
```

Here:

```text
101
```

is the path parameter.

FastAPI automatically extracts the value and passes it to the function.

Example:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

---

## 📌 When to Use Path Parameters

Use path parameters when identifying a specific resource.

Examples:

```text
/users/101
/products/500
/orders/1001
/students/25
```

Think:

```text
Which resource do I want?
```

---

## 🔎 Query Parameters

Query parameters are passed after the `?` symbol.

Example:

```text
/products?limit=5
```

Here:

```text
limit=5
```

is a query parameter.

Example:

```python
@app.get("/products")
def get_products(limit: int = 5):
    return {"limit": limit}
```

---

## 📌 When to Use Query Parameters

Use query parameters when filtering or customizing results.

Examples:

```text
/products?limit=5

/products?category=electronics

/users?city=mumbai

/search?keyword=laptop
```

Think:

```text
How should the result be filtered?
```

---

## ⚖️ Path Parameters vs Query Parameters

### Path Parameter

```text
/products/101
```

Purpose:

```text
Identify a specific resource
```

---

### Query Parameter

```text
/products?limit=5
```

Purpose:

```text
Filter or customize the response
```

---

### Combined Example

```text
/products/101?currency=USD
```

Explanation:

```text
101            → Path Parameter
currency=USD   → Query Parameter
```

---

## ✅ Parameter Validation

FastAPI can automatically validate incoming parameters.

Example:

```python
from fastapi import Query

limit: int = Query(
    default=5,
    ge=1,
    le=10
)
```

Meaning:

```text
1 <= limit <= 10
```

---

## 🔤 String Validation

Example:

```python
keyword: str = Query(
    min_length=3,
    max_length=20
)
```

Meaning:

```text
3 <= keyword length <= 20
```

---

## 📖 Swagger and Parameters

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger automatically displays:

- Parameter names
- Data types
- Default values
- Validation rules
- Descriptions

This makes APIs easier to understand and test.

---

## ❌ Common Mistakes

### Using Path Parameters for Filtering

Bad:

```text
/products/electronics
```

when the goal is filtering.

Better:

```text
/products?category=electronics
```

---

### Using Query Parameters for Resource Identification

Bad:

```text
/product?id=101
```

Better:

```text
/ products/101
```

---

## ✅ Session Summary

In this session, you learned:

- Path Parameters
- Query Parameters
- Combining Path and Query Parameters
- Parameter Validation
- FastAPI Query()
- Common parameter design patterns

You can now build dynamic API endpoints that accept and validate user input.