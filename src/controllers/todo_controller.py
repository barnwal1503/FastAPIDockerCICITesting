from typing import Annotated

from fastapi import Query

from src.dependencies import TodoServiceDep
from src.models.todo import Todo
from src.schemas.todo import TodoCreate, TodoListResponse, TodoUpdate


def list_todos(
    service: TodoServiceDep,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    offset: Annotated[int, Query(ge=0)] = 0,
    completed: bool | None = None,
) -> TodoListResponse:
    items, total = service.list(limit=limit, offset=offset, completed=completed)
    return TodoListResponse(items=items, total=total, limit=limit, offset=offset)


def get_todo(todo_id: int, service: TodoServiceDep) -> Todo:
    return service.get(todo_id)


def create_todo(payload: TodoCreate, service: TodoServiceDep) -> Todo:
    return service.create(payload)


def update_todo(todo_id: int, payload: TodoUpdate, service: TodoServiceDep) -> Todo:
    return service.update(todo_id, payload)


def delete_todo(todo_id: int, service: TodoServiceDep) -> None:
    service.delete(todo_id)
