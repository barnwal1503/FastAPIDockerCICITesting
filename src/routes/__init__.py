from fastapi import APIRouter

from src.routes import health_routes, pages_routes, todo_routes

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(todo_routes.router)

router = APIRouter()
router.include_router(pages_routes.router)
router.include_router(health_routes.router)
router.include_router(api_v1_router)
