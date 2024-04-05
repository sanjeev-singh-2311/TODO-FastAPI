from pydantic import BaseModel

class TodoWithoutID(BaseModel):
    body : str
    status : bool = False

class Todo(TodoWithoutID):
    id : int


    
