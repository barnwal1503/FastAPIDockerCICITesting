from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError
from src.models.todo import Todo
from src.schemas.todo import TodoCreate, TodoUpdate


class TodoService:
    def __init__(self, db: Session):
        self.db = db

    def list(
        self, *, limit: int, offset: int, completed: bool | None = None
    ) -> tuple[list[Todo], int]:
        query = select(Todo)
        if completed is not None:
            query = query.where(Todo.completed == completed)

        total = self.db.scalar(select(func.count()).select_from(query.subquery())) or 0
        items = self.db.scalars(
            query.order_by(Todo.created_at.desc(), Todo.id.desc()).limit(limit).offset(offset)
        ).all()
        return list(items), total

    def get(self, todo_id: int) -> Todo:
        todo = self.db.get(Todo, todo_id)
        if todo is None:
            raise NotFoundError(f"Todo {todo_id} not found")
        return todo

    def create(self, data: TodoCreate) -> Todo:
        todo = Todo(**data.model_dump())
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def update(self, todo_id: int, data: TodoUpdate) -> Todo:
        todo = self.get(todo_id)
        for field, value in data.model_dump().items():
            setattr(todo, field, value)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def delete(self, todo_id: int) -> None:
        todo = self.get(todo_id)
        self.db.delete(todo)
        self.db.commit()
