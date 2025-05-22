# Import FastAPI class to create the web app
from fastapi import FastAPI
from . import schemas

# Create an instance of the FastAPI app
app = FastAPI()

@app.post('/blog')
def create(request: schemas.Blog):
    # The request parameter is automatically parsed & validated as a Blog object
    # The function returns the entire Blog object back as the response (JSON)
    return request

