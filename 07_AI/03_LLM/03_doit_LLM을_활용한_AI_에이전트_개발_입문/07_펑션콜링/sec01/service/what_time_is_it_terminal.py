# what_time_is_it_terminal.py
from tools.gpt_functions import get_current_time, tools
from openai import OpenAI
from config.config import config
import json

client = OpenAI(api_key = config["apikey"]["openai"])

# chat gpt로부터 응답을 받아오는 기본적인 틀
def get_ai_response(messages, tools=None):
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = messages,
        tools = tools
    )
    return response

# 기본 초기 메시지 셋
messages = [
    {"role" : "system", "content" : "너는 사용자를 도와주는 상담사야."},
]

# 터미널 대화 섹션
def terminal_conversation():
    while True:
        # 사용자 입력 발화
        user_input = input("사용자\t:")
        if user_input == "exit":
            break
        
        # 메시지 셋에 사용자 발화 입력
        messages.append({"role":"user", "content":user_input})
        
        # chat gpt에거 답변 받아옴
        ai_response = get_ai_response(messages=messages,
                                    tools=tools)
        ai_message = ai_response.choices[0].message
        
        # tool_calls
        tool_calls = ai_message.tool_calls
        if tool_calls:
            for tool_call in tool_calls: # ---- (1) tool call 마다 반복
                # 도구 정보 추출
                tool_name = tool_call.function.name
                tool_call_id = tool_call.id
                
                print(tool_call.function)
                arguments = json.loads(tool_call.function.arguments) 
                
                # 도구마다 사용 함수 매칭해서 도구의 결과를 메시지로 생성
                if tool_name == "get_current_time":
                    messages.append(
                        {
                            "role" : "function",
                            "tool_call_id" : tool_call_id,
                            "name" : tool_name,
                            "content" : get_current_time(timezone=arguments["timezone"]), 
                        }
                    )
            
            messages.append({"role":"system", "content":"이제 주어진 결과들을 바탕으로 답변하시오"}) # ------ (2) tool call 이 끝났으니, 답변하도록 함        
            # 한번 더 gpt 응답 호출, 이번엔 도구의 결과와 도구 호출 id를 포함함
            ai_response = get_ai_response(messages, tools=tools)
            ai_message = ai_response.choices[0].message
        print(ai_message)
        messages.append(ai_message)
        print("AI\t:" + ai_message.content)