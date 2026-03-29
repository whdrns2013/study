# gpt_function.py
from tools import _get_current_time, _get_yf_stock_info, _get_yf_stock_history, _get_yf_stock_recommendations

tools = [
    _get_current_time.tool_def,
    _get_yf_stock_info.tool_def,
    _get_yf_stock_history.tool_def,
    _get_yf_stock_recommendations.tool_def
]

def tool_mapping(messages:list[dict],
                 tool_name:str,
                 tool_call_id:str|int,
                 arguments:dict|None):
    if tool_name == "get_current_time":
        func_result = _get_current_time.func(timezone=arguments["timezone"])
    elif tool_name == "get_yf_stock_info":
        func_result = _get_yf_stock_info.func(ticker=arguments["ticker"])
    elif tool_name == "get_yf_stock_history":
        func_result = _get_yf_stock_history.func(ticker=arguments["ticker"], period=arguments["period"])
    elif tool_name == "get_yf_stock_recommendations":
        func_result = _get_yf_stock_recommendations.func(ticker=arguments["ticker"])
    
    messages.append(
        {
            "role" : "function",
            "tool_call_id" : tool_call_id,
            "name" : tool_name,
            "content" : func_result, 
        }
    )
    
    return messages