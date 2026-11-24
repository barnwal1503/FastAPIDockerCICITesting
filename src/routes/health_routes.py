from fastapi import APIRouter

from src.controllers import health_controller

router = APIRouter(tags=["health"])

router.add_api_route("/health", health_controller.health, methods=["GET"])
