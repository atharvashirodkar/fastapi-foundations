# FastAPI Foundation 🚀

A comprehensive, hands-on learning resource for mastering **FastAPI** — a modern, fast web framework for building APIs with Python. This repository provides structured tutorials, practical examples, and a complete mini-project to help you progress from beginner to intermediate FastAPI developer.

---

## 📘 Project Overview

**FastAPI Foundation** is a step-by-step guide to learning FastAPI, one of the fastest and most developer-friendly frameworks for building production-ready APIs in Python. Whether you're new to web development or transitioning from another framework, this project walks you through core concepts with clear examples and real-world patterns.

### What's Inside

- **8 Progressive Learning Modules** – From basic setup to advanced routing patterns
- **30+ Working Code Examples** – Copy, run, and modify real FastAPI applications
- **Complete Mini Project** – A fully functional Student Management System API
- **Best Practices** – Learn patterns for request validation, response modeling, and API organization
- **Ready to Run** – All examples are executable and documented

---

## 💡 Why It Matters

**FastAPI** is reshaping how developers build APIs in Python because it:

- ⚡ **Is Fast** – High performance comparable to Node.js and Go
- 🧪 **Reduces Bugs** – Automatic data validation and serialization with Pydantic
- 📖 **Auto-Generates Docs** – Interactive API documentation (Swagger UI) out of the box
- 🎯 **Is Modern** – Built on modern Python standards (type hints, async/await)
- 🔒 **Is Secure** – Built-in support for OAuth2, JWT, and CORS

This foundation course ensures you understand FastAPI deeply, setting you up for building robust production applications.

---

## ⚙️ Getting Started

### Prerequisites

- **Python 3.7+** installed on your system
- **pip** (Python package manager)
- A text editor or IDE (VS Code, PyCharm, etc.)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-foundation
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn pydantic
   ```

3. **Run an example**
   ```bash
   cd 01_fastapi_intro
   uvicorn 02_intro_app:app --reload
   ```

4. **Open in browser**
   - Visit `http://localhost:8000` to see the API
   - Visit `http://localhost:8000/docs` for interactive documentation

---

## 🧩 Project Structure & Learning Path

Each module builds on the previous one. Follow this sequence for best results:

### 1️⃣ **01_fastapi_intro** – Your First App
Learn to set up FastAPI and create your first "Hello World" API.
- Basic application setup
- Creating simple routes
- Running the development server

**Key Files:**
- `02_intro_app.py` – Start here!

### 2️⃣ **02_routes** – Mastering Routes
Understand HTTP methods and route organization.
- GET, POST, PUT, DELETE operations
- Route ordering and specificity
- Adding metadata to routes

### 3️⃣ **03_parameters** – Path & Query Parameters
Accept user input through URLs.
- Path parameters: `/users/{user_id}`
- Query parameters: `/users?skip=0&limit=10`
- Parameter validation and types

### 4️⃣ **04_request_body** – Handling Data
Accept structured data in request bodies.
- Basic request bodies
- Multiple fields and complex data

### 5️⃣ **05_pydantic** – Data Validation
Master Pydantic models for robust data handling.
- Creating Pydantic models
- Optional fields and defaults
- Field constraints and validation
- Nested models

### 6️⃣ **06_response_models** – Shaping Responses
Control what data is returned to clients.
- Response models
- Field filtering
- List responses
- Response model best practices

### 7️⃣ **07_crud_api** – Building Real APIs
Create complete Create, Read, Update, Delete APIs.
- Read operations (GET)
- Create operations (POST)
- Update operations (PUT)
- Delete operations (DELETE)
- Complete CRUD example with in-memory database

### 8️⃣ **08_routers** – Organizing Code
Structure larger APIs with routers and modular design.
- Single router implementation
- Multiple routers
- Router prefixes and tags
- Package-based organization

### 🎓 **mini_projects/student_management_system** – Capstone Project
Apply all concepts to build a complete API:
- Manage students, courses, and marks
- RESTful endpoints
- Modular router architecture
- In-memory persistence

---

## 🚀 Quick Examples

### Run a Basic API
```bash
cd 01_fastapi_intro
uvicorn 02_intro_app:app --reload
```

### Run the Complete Student Management System
```bash
cd mini_projects/student_management_system
uvicorn main:app --reload
```

### Create Your First Endpoint
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Run with: uvicorn filename:app --reload
```

---

## 📚 Understanding the Code

### Each Module Includes:

- **Python Files** – Progressively complex working examples
- **notes.md** – Key concepts and explanations
- **Comments** – Inline explanations for clarity

### Example: Route Parameters
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int, skip: int = 0, limit: int = 10):
    return {
        "user_id": user_id,
        "skip": skip,
        "limit": limit
    }
```

---

## 🧠 Key Concepts Covered

| Concept | Module | Files |
|---------|--------|-------|
| Basic API Setup | 01 | `02_intro_app.py` |
| Routes & HTTP Methods | 02 | `02_route_methods.py` |
| Path Parameters | 03 | `01_path_parameters.py` |
| Query Parameters | 03 | `02_query_parameters.py` |
| Request Bodies | 04 | `01_basic_request_body.py` |
| Pydantic Models | 05 | `01_first_model.py` |
| Response Models | 06 | `01_basic_response_model.py` |
| CRUD Operations | 07 | `05_complete_crud_api.py` |
| Code Organization | 08 | `04_router_package/` |

---

## 🔗 Useful Resources

- **Official FastAPI Docs**: https://fastapi.tiangolo.com/
- **Pydantic Documentation**: https://docs.pydantic.dev/
- **Uvicorn Guide**: https://www.uvicorn.org/
- **Python Type Hints**: https://docs.python.org/3/library/typing.html

---

## 🛠️ Requirements

```
fastapi         # Web framework
uvicorn         # ASGI server
pydantic        # Data validation
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 💬 Contributing & Support

This is a learning resource! Contributions and improvements are welcome:

- Found an issue? Create a GitHub issue
- Have improvements? Submit a pull request
- Want to add examples? Contributions are appreciated

For questions or feedback about the material, open an issue or contact the maintainer mentioned below.

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🎯 Next Steps

1. **Start Here**: Go to `01_fastapi_intro/02_intro_app.py` and run it
2. **Follow the Path**: Progress through modules 01-08 sequentially
3. **Experiment**: Modify examples and build your own endpoints
4. **Build**: Complete the Student Management System mini-project
5. **Create**: Build your own FastAPI project using these patterns

---

## 👨‍💻 Author

Created and maintained by **Atharva Shirodkar**  
GitHub: [@atharvashirodkar](https://github.com/atharvashirodkar)

Maintained the FastAPI Foundation learning repository.

---

**Happy Learning! 🎓**

*Start with the basics, practice consistently, and you'll master FastAPI in no time.*
