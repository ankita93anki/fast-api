# Import BaseModel from Pydantic to define data schemas (for validation & parsing)
from pydantic import BaseModel

# Define a data model for the blog using Pydantic
class Blog(BaseModel):
    title: str
    body: str