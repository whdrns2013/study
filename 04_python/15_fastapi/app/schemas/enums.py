from typing import Literal
from enum import Enum

class StatusCode(str, Enum):
    SUCCESS="0"
    FAIL="1"