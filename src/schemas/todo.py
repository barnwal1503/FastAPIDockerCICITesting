from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TodoBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=2000)


class TodoCreate(TodoBase):
    completed: bool = False


class TodoUpdate(TodoBase):
    completed: bool


class TodoRead(TodoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime


class TodoListResponse(BaseModel):
    items: list[TodoRead]
    total: int
    limit: int
    offset: int
