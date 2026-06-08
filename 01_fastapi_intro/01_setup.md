# FastAPI Setup

Before building APIs with FastAPI, set up a virtual environment and install the required packages.

## Prerequisites

Make sure Python is installed on your system.

Check the installed version:

```bash
python --version
```

Example output:

```text
Python 3.12.0
```

---

## Create a Virtual Environment

Open a terminal in the project directory and run:

```bash
python -m venv venv
```

This creates an isolated Python environment named `venv`.

Project structure:

```text
project/
│
├── venv/
└── ...
```

---

## Activate the Virtual Environment

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows (Command Prompt)

```cmd
venv\Scripts\activate.bat
```

### Linux / macOS

```bash
source venv/bin/activate
```

After activation, your terminal should display:

```text
(venv)
```

at the beginning of the command line.

---

## Install FastAPI

Install FastAPI using pip:

```bash
pip install fastapi
```

---

## Install Uvicorn

Uvicorn is an ASGI server used to run FastAPI applications.

Install Uvicorn:

```bash
pip install uvicorn
```

---

## Verify Installation

Check that FastAPI is installed:

```bash
pip show fastapi
```

Check that Uvicorn is installed:

```bash
pip show uvicorn
```

---

## View Installed Packages

```bash
pip list
```

Example output:

```text
fastapi
uvicorn
pydantic
starlette
```

---

## Deactivate the Virtual Environment

When you are done working on the project:

```bash
deactivate
```

---

## Summary

In this setup guide, you learned how to:

- Create a virtual environment
- Activate a virtual environment
- Install FastAPI
- Install Uvicorn
- Verify package installation
- Deactivate the virtual environment

You are now ready to create your first FastAPI application.