# Import the FastAPI class to create the app instance
from fastapi import FastAPI 

# Create a FastAPI application instance
app = FastAPI()

# Define a route for GET requests at the root URL "/
@app.get("/")
def index():
    return {'data': {'name': 'Sarthak'}} # Return a JSON response 

@app.get("/about")
def about():
    return {'data' : {'name': 'Ankita is working in Google'}}
