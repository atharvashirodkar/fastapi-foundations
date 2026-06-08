# 🚀 Running a FastAPI Application

Now that the application has been created, it's time to run the FastAPI server and test the available routes.

---

## ▶️ Start the Development Server

Open a terminal inside the `01_fastapi_intro` folder and run:

```bash
uvicorn 02_intro_app:app --reload
```

---

## 🔍 Understanding the Command

```text
uvicorn
```

Runs the ASGI server.

```text
02_intro_app
```

The Python file name (without `.py`).

```text
app
```

The FastAPI application instance.

```text
--reload
```

Automatically restarts the server whenever code changes are detected.

---

## ✅ Expected Output

If everything works correctly, you should see output similar to:

```text
INFO:     Will watch for changes in these directories
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started reloader process
INFO:     Started server process
```

---

## 🌐 Test the Routes

Open the following URLs in your browser.

### Home Route

```text
http://127.0.0.1:8000/
```

Response:

```json
{
  "message": "Welcome to FastAPI"
}
```

---

### About Route

```text
http://127.0.0.1:8000/about
```

Response:

```json
{
  "message": "About Page"
}
```

---

### Contact Route

```text
http://127.0.0.1:8000/contact
```

Response:

```json
{
  "message": "Contact Page"
}
```

---

## 📖 Interactive API Documentation

One of FastAPI's best features is automatic API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

- View all endpoints
- Read endpoint documentation
- Test APIs directly from the browser

---

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

ReDoc provides a cleaner, documentation-focused view of the API.

---

## 🛑 Stop the Server

Press:

```text
CTRL + C
```

in the terminal.

This will stop the running server.

---

## ✅ Summary

In this lesson, you learned how to:

- Run a FastAPI application using Uvicorn
- Understand the Uvicorn command
- Access application routes
- Use Swagger UI
- Use ReDoc
- Stop the development server

You are now ready to build more routes and explore FastAPI features.