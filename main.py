# Import the FastAPI class to create the app instance
from fastapi import FastAPI 
# Create a FastAPI application instance
myapp = FastAPI()

# Define a route for GET requests at the root URL "/
@myapp.get("/")
def index():
    return {'data': {'name': 'Sarthak'}} # Return a JSON response 

@myapp.get("/about")
def about():
    return {'data' : {'name': 'Ankita is working in Google'}}
