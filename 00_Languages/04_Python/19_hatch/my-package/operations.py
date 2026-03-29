from .models import Operands

def add(data: Operands) -> int | float:
    return data.a + data.b

def sub(data: Operands) -> int | float:
    return data.a - data.b

def mul(data: Operands) -> int | float:
    return data.a * data.b

def div(data: Operands) -> int | float:
    if data.b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return data.a / data.b
