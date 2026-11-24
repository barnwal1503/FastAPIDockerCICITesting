from sqlalchemy import String, Text, false
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base, TimestampMixin


class Todo(TimestampMixin, Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    completed: Mapped[bool] = mapped_column(
        default=False, server_default=false(), nullable=False, index=True
    )
