# 📝 FastAPI Notes

## 📌 What is FastAPI?

FastAPI is a modern Python web framework used to build APIs quickly and efficiently.

It is built on top of:

- Starlette (Web Framework)
- Pydantic (Data Validation)

---

## 🚀 Why FastAPI?

FastAPI is popular because it provides:

- High performance
- Easy-to-read code
- Automatic API documentation
- Built-in data validation
- Type hint support

Example:

```python
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
```

---

## 📌 What is an API?

API stands for:

```text
Application Programming Interface
```

An API allows different applications to communicate with each other.

Example:

```text
Browser
   ↓
FastAPI Server
   ↓
Database
```

When a user visits a URL, the API processes the request and returns a response.

---

## 📌 What is a Route?

A route is a URL path that performs a specific action.

Example:

```python
@app.get("/")
def home():
    return {"message": "Welcome"}
```

Route:

```text
/
```

Example:

```python
@app.get("/about")
def about():
    return {"message": "About Page"}
```

Route:

```text
/about
```

---

## 📌 What is a Request?

A request is sent by a client to a server.

Examples:

```text
GET /
GET /about
GET /contact
```

The browser sends requests whenever a URL is visited.

---

## 📌 What is a Response?

A response is returned by the server.

Example:

```json
{
  "message": "Welcome to FastAPI"
}
```

FastAPI automatically converts Python dictionaries into JSON responses.

---

## 📌 What is JSON?

JSON stands for:

```text
JavaScript Object Notation
```

JSON is the most common format used for exchanging data between applications.

Example:

```json
{
  "name": "Rahul",
  "age": 22
}
```

---

## 📌 What is Uvicorn?

Uvicorn is an ASGI server used to run FastAPI applications.

Example:

```bash
uvicorn 02_intro_app:app --reload
```

Without Uvicorn, the FastAPI application cannot serve requests.

---

## 📌 What is Swagger UI?

Swagger UI is an automatically generated interface for testing APIs.

URL:

```text
http://127.0.0.1:8000/docs
```

Benefits:

- View endpoints
- Test APIs
- Read documentation

---

## 📌 What is ReDoc?

ReDoc is another automatically generated documentation interface.

URL:

```text
http://127.0.0.1:8000/redoc
```

It provides a cleaner and more documentation-focused layout.

---

## ✅ Session Summary

In this session, you learned:

- What FastAPI is
- What an API is
- What routes are
- What requests and responses are
- What JSON is
- What Uvicorn is
- What Swagger UI is
- What ReDoc is

You are now ready to create and work with routes in FastAPI.