from fastapi import APIRouter
from app.api.v1.endpoints.health_check import health_check_router
from core.settings import settings

routers = APIRouter(prefix=settings.ENDPOINT.PREFIX)

routers.include_router(health_check_router)