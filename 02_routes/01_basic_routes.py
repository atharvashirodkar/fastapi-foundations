from fastapi import FastAPI

app = FastAPI()


# Home route
@app.get("/")
def home():
    return {"message": "Home Page"}


# About route
@app.get("/about")
def about():
    return {"message": "About Page"}


# Contact route
@app.get("/contact")
def contact():
    return {"message": "Contact Page"}