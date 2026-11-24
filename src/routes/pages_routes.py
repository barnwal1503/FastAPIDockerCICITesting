from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from src.controllers import pages_controller

router = APIRouter(tags=["pages"])

router.add_api_route("/", pages_controller.root, methods=["GET"])
router.add_api_route(
    "/portfolio", pages_controller.portfolio, methods=["GET"], response_class=HTMLResponse
)
