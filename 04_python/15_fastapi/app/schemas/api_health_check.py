from pydantic import BaseModel
from app.schemas.enums import StatusCode

class HealthCheckResponse(BaseModel):
    status_code:StatusCode
    error_message:str