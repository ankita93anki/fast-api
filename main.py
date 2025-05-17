# Import the FastAPI class to create the app instance
from fastapi import FastAPI 
from typing import Optional
# Create a FastAPI application instance
myapp = FastAPI()

# Define a route for GET requests at the root URL "/
@myapp.get("/")
def index():
    return {'data': 'blog list'} # Return a JSON response 

@myapp.get('/blog')
def blog(limit = 10, published:bool = True, sort: Optional[str]=None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@myapp.get('/blog/unpublished')
def unpublished():
    return {'data' : "all unpublished blogs"}

@myapp.get("/blog/{id}")
def show(id: int):
    #fetch blog with id
    return {'data' : id}

@myapp.get('/blog/{id}/comments')
def comments(id):
    #fetch comment of a blog with id
    return {'data': {'1','2'}}

