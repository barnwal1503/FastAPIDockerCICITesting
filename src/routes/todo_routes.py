from fastapi import APIRouter, status

from src.controllers import todo_controller
from src.schemas.todo import TodoListResponse, TodoRead

router = APIRouter(prefix="/todos", tags=["todos"])

router.add_api_route(
    "", todo_controller.list_todos, methods=["GET"], response_model=TodoListResponse
)
router.add_api_route(
    "/{todo_id}", todo_controller.get_todo, methods=["GET"], response_model=TodoRead
)
router.add_api_route(
    "",
    todo_controller.create_todo,
    methods=["POST"],
    response_model=TodoRead,
    status_code=status.HTTP_201_CREATED,
)
router.add_api_route(
    "/{todo_id}", todo_controller.update_todo, methods=["PUT"], response_model=TodoRead
)
router.add_api_route(
    "/{todo_id}",
    todo_controller.delete_todo,
    methods=["DELETE"],
    status_code=status.HTTP_204_NO_CONTENT,
)
