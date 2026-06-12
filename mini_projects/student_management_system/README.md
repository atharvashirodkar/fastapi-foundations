# Student Management System

A lightweight, RESTful API built with FastAPI for managing students, courses, and academic marks. This project demonstrates modern Python web development with data validation, modular routing, and JSON-based persistence.

---

## 📘 Project Overview

**Student Management System** is a FastAPI-based backend application that provides a complete CRUD (Create, Read, Update, Delete) interface for educational data management. It enables administrators and educators to efficiently manage student records, course catalogs, and academic performance tracking through a clean REST API.

### Key Capabilities
- **Student Management** – Register and track student information with validation
- **Course Administration** – Create and organize course offerings
- **Mark Tracking** – Record and retrieve student performance data
- **Data Filtering** – Query students by age, courses by name, and marks by student
- **RESTful Design** – Standards-compliant API endpoints with proper HTTP methods
- **Input Validation** – Pydantic-powered request/response schema validation

---

## 💡 Why It Matters

This project is ideal for:
- **Learning FastAPI** – A practical example of API design patterns, routing, and validation
- **Educational Technology** – A foundation for building larger student information systems (SIS)
- **Data Management** – Understanding JSON-based persistence and CRUD operations
- **Rapid Prototyping** – Quickly mock or test educational workflows

The modular architecture makes it easy to extend with new features like authentication, database integration, or reporting.

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone or download the repository**
   ```bash
   cd student_management_system
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

**Interactive API Documentation:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## 📚 API Endpoints

### Students (`/students`)
- `GET /students` – Retrieve all students
  - Query parameter: `age` (optional) – Filter by student age
  ```bash
  curl http://localhost:8000/students
  curl http://localhost:8000/students?age=20
  ```

- `GET /students/{student_id}` – Get a specific student
  ```bash
  curl http://localhost:8000/students/1
  ```

- `POST /students` – Create a new student
  ```bash
  curl -X POST http://localhost:8000/students \
    -H "Content-Type: application/json" \
    -d '{"name": "John Doe", "age": 20}'
  ```

### Courses (`/courses`)
- `GET /courses` – Retrieve all courses
  - Query parameter: `name` (optional) – Search by course name
  ```bash
  curl http://localhost:8000/courses
  curl http://localhost:8000/courses?name=Math
  ```

- `GET /courses/{course_id}` – Get a specific course
  ```bash
  curl http://localhost:8000/courses/1
  ```

- `POST /courses` – Create a new course
  ```bash
  curl -X POST http://localhost:8000/courses \
    -H "Content-Type: application/json" \
    -d '{"name": "Mathematics 101"}'
  ```

### Marks (`/marks`)
- `GET /marks` – Retrieve all marks
  ```bash
  curl http://localhost:8000/marks
  ```

- `GET /marks/student/{student_id}` – Get marks for a specific student
  ```bash
  curl http://localhost:8000/marks/student/1
  ```

- `POST /marks` – Record a student's mark for a course
  ```bash
  curl -X POST http://localhost:8000/marks \
    -H "Content-Type: application/json" \
    -d '{"student_id": 1, "course_id": 1, "marks": 85}'
  ```

---

## 📂 Project Structure

```
student_management_system/
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── data/                      # JSON data storage
│   ├── students.json         # Student records
│   ├── courses.json          # Course records
│   └── marks.json            # Academic marks
├── models/
│   ├── __init__.py
│   └── models.py             # Pydantic data models
└── routers/
    ├── __init__.py
    ├── students.py           # Student endpoints
    ├── courses.py            # Course endpoints
    └── marks.py              # Marks endpoints
```

---

## 🛠️ Data Models

### Student
```json
{
  "id": 1,
  "name": "John Doe",
  "age": 20
}
```
- `name`: 2+ characters required
- `age`: Positive integer required

### Course
```json
{
  "id": 1,
  "name": "Mathematics 101"
}
```
- `name`: 2+ characters required

### Mark
```json
{
  "student_id": 1,
  "course_id": 1,
  "marks": 85
}
```
- `marks`: Integer between 0 and 100 required

---

## 🧩 Documentation & Support

- **FastAPI Documentation:** [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **Pydantic Validation:** [https://docs.pydantic.dev/](https://docs.pydantic.dev/)
- **Uvicorn Server:** [https://www.uvicorn.org/](https://www.uvicorn.org/)

For questions or issues, please check the project's issue tracker or documentation.

---

## 👥 Maintainers & Contributors

This project is maintained by the FastAPI community. Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

---

## 📝 License

This project is open-source and available under the MIT License. See the LICENSE file for details.

---

## 🚀 Next Steps

**Potential Enhancements:**
- Add database integration (PostgreSQL, MongoDB)
- Implement authentication and authorization
- Add error handling and logging
- Create unit and integration tests
- Deploy to cloud services (AWS, GCP, Azure)
- Add OpenAPI/Swagger schema documentation

---

## 👨‍💻 Author

Created and maintained by **Atharva Shirodkar**  
GitHub: [@atharvashirodkar](https://github.com/atharvashirodkar)

Maintained the FastAPI Foundation learning repository.

---

**Happy Learning! 🎓**

*Start with the basics, practice consistently, and you'll master FastAPI in no time.*
