from pydantic import BaseModel

class LogSenderSchema(BaseModel):
    system: str
    date_time: str
    message: str