from typing import Annotated, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schema import Todo, TodoWithoutID
from .models import Todo
from .dependencies import get_db

app_router = APIRouter(
        prefix='/app',
        tags=['TODO']
        )

todo : list[Todo] = []

@app_router.get('/')
async def get_all_todo(*, session : Annotated[Session, Depends(get_db)]) -> dict[int, Any]:
    datas : list[Todo] = session.query(Todo).all()
    result = {}
    for data in datas:
        result.update({data.id : TodoWithoutID(**data.__dict__)})

    return result


@app_router.post('/')
async def add_new_todo(*, item : str, session : Annotated[Session, Depends(get_db)]):
    new_todo = Todo(body=item)
    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)
    return {'message' : 'Success'}

@app_router.put('/{id}')
async def change_todo_status(*, id : int, session : Annotated[Session, Depends(get_db)]):

    todo = session.query(Todo).where(Todo.id == id).first()
    
    if not todo:
        return {'message' : 'Todo not found'} 
    
    todo.status = not todo.status
    session.commit()
    session.refresh(todo)
    return {'message' : 'Todo updated successfully'}

@app_router.delete('/{id}')
async def delete_todo(*, id : int, session : Annotated[Session, Depends(get_db)]):

    todo = session.query(Todo).where(Todo.id == id).first()
    session.delete(todo)
    session.commit()
    return {'message' : 'Todo successfully deleted'}
