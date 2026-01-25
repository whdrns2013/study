from pydantic import BaseModel

class Operands(BaseModel):
    a: int | float
    b: int | float