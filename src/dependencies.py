from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.services.todo_service import TodoService

DbSession = Annotated[Session, Depends(get_db)]


def get_todo_service(db: DbSession) -> TodoService:
    return TodoService(db)


TodoServiceDep = Annotated[TodoService, Depends(get_todo_service)]
