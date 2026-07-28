from fastapi import APIRouter
from app.core.settings import settings
from app.schemas.api_health_check import HealthCheckResponse

health_check_router = APIRouter()

@health_check_router.get(settings.ENDPOINT.HEALTHCHECK)
def health_check():
    return HealthCheckResponse(status_code="0", error_message="")