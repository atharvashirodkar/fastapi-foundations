from fastapi import FastAPI

# Create a FastAPI application instance
app = FastAPI()


# Home route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


# About route
@app.get("/about")
def about():
    return {"message": "About Page"}


# Contact route
@app.get("/contact")
def contact():
    return {"message": "Contact Page"}