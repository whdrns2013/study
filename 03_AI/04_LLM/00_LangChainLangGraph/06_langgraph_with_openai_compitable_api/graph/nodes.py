import random
from graph.state import AppState
import time
from langgraph.config import get_stream_writer

def input_routing_function(state:AppState):
    return state["input"] < 0

# def input_routing_function(state:AppState):
#     writer = get_stream_writer()
#     writer(f"사용자의 입력 : {state['input']}\n")
#     return state["input"] < 0

# 1차
# def generate_node(state:AppState):
#     progress = "임의의 숫자 생성중"
#     return {"value" : random.randint(1, 100), "count" : state["count"] + 1, "step":progress}

def generate_node(state:AppState):
    value = random.randint(1, 100)
    count = state["count"] + 1 
    progress = f"임의의 숫자 생성 ({count}회차) : {value}\n"
    writer = get_stream_writer()
    writer(progress)
    return {"value" : value, "count" : count, "step":progress}

# 1차
def routing_function(state:AppState):
    time.sleep(random.randint(2, 15)/10)
    return state["input"] > state["value"]

# def routing_function(state:AppState):
#     result = state["input"] > state["value"]
#     writer = get_stream_writer()
#     if result:
#         writer(f"사용자가 입력한 값이 생성된 {state['value']}보다 큽니다.\n")
#     else:
#         writer(f"사용자가 입력한 값이 생성된 {state['value']}보다 작아, 숫자를 다시 생성합니다.\n")
#     time.sleep(random.randint(2, 15)/10)
#     return result

# 1차
# def terminate_node(state:AppState):
#     if "value" not in state.keys():
#         return {"response" : f"사용자가 입력한 {state['input']}은(는) 0보다 작습니다."}
#     return {"response" : f"{state['count']} 번 반복 실행됐습니다."}

def terminate_node(state:AppState):
    writer = get_stream_writer()
    
    if "value" not in state.keys():
        chunks = ["사용자가 ", "입력한 ", f"{state['input']}", "은(는) ", "0보다", " ", "작습니다."]
    else:
        chunks = [f"{state['count']} ", "번 ", "반복 ", "실행됐", "습니다."]
    
    full_text = ""
    
    for chunk in chunks:
        writer(chunk)
        time.sleep(random.randint(1, 10)/10)
        full_text += chunk
    
    return {"response" : full_text}