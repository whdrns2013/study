# 파일명 : tools/gpt_functions.py
from tools import _get_current_time, _get_yf_stock_info, _get_yf_stock_history, _get_yf_stock_recommendations

# 사용 가능한 도구(펑션)들에 대한 설명 정보 리스트
tools = [
    _get_current_time.tool_def,
    _get_yf_stock_info.tool_def,
    _get_yf_stock_history.tool_def,
    _get_yf_stock_recommendations.tool_def
]

# 도구(펑션) 이름과 실행할 함수 매팽
def tool_mapping(tool_name:str, arguments:dict|None):
    if tool_name == "get_current_time":
        func_result = _get_current_time.func(timezone=arguments["timezone"])
    elif tool_name == "get_yf_stock_info":
        func_result = _get_yf_stock_info.func(ticker=arguments["ticker"])
    elif tool_name == "get_yf_stock_history":
        func_result = _get_yf_stock_history.func(ticker=arguments["ticker"], period=arguments["period"])
    elif tool_name == "get_yf_stock_recommendations":
        func_result = _get_yf_stock_recommendations.func(ticker=arguments["ticker"])
    return func_result
