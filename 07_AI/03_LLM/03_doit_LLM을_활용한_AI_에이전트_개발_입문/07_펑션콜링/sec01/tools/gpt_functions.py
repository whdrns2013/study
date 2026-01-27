# gpt_function.py
from datetime import datetime
import pytz

def get_current_time(timezone="Asia/Seoul"):
    tz = pytz.timezone(timezone)
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    now_timezone = f"{now} {timezone}"
    return now_timezone

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "해당 타임존의 날짜와 시간을 반환합니다.",
            "parameters": {
                "type":"object",
                "properties":{
                    "timezone": {
                        "type":"string",
                        "description":"현재 날짜와 시간을 반환할 타임존을 입력하세요.(예. Aisa/Seoul)",
                    }
                },
                "required":["timezone"]
            }
        }
    },
]

def tool_mapping(messages:list[dict],
                 tool_name:str,
                 tool_call_id:str|int,
                 arguments:dict|None):
    if tool_name == "get_current_time":
        messages.append(
            {
                "role" : "function",
                "tool_call_id" : tool_call_id,
                "name" : tool_name,
                "content" : get_current_time(timezone=arguments["timezone"]), 
            }
        )
    return messages