from tools.gpt_functions import get_current_time, tools
from openai import OpenAI
from config.config import config

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
while True:
    # 사용자 입력 발화
    user_input = input("사용자\t:")
    if user_input == "exit":
        break
    
    # 메시지 셋에 사용자 발화 입력
    messages.append({"role":"user", "content":user_input})
    
    # chat gpt에거 답변 받아옴
    ai_response = get_ai_response(messages=messages,
                                  tools=tools) # 사용 가능한 도구 목록 제공
    ai_message = ai_response.choices[0].message
    print(ai_message)
    
    # tool_calls
    tool_calls = ai_message.tool_calls
    # gpt가 특정 함수 실행이 필요하다고 판단할 경우, 응답의 tool_calls 속성에 정보가 포함됨 #TODO: 메시지 구조 확인
    if tool_calls:
        # 도구 정보 추출 #TODO: tool_calls 리스폰스 구조 확인
        tool_name = tool_calls[0].function.name
        tool_call_id = tool_calls[0].id #TODO: id가 무슨 역할을 하는지 확인하고 스터디때 발표
        # 도구마다 사용 함수 매칭해서 도구의 결과를 메시지로 생성
        if tool_name == "get_currnet_time":
            messages.append(
                {
                    "role" : "function",
                    "tool_call_id" : tool_call_id, # 여기에 id를 매칭시켜서 gpt 자신이 요청한 도구 호출과 결과물을 매칭
                    "name" : tool_name,
                    "content" : get_current_time(),
                }
            )
        # 한번 더 gpt 응답 호출, 이번엔 도구의 결과와 도구 호출 id를 포함함
        ai_response = get_ai_response(messages, tools=tools)
        ai_message = ai_response.choices[0].message
        
    messages.append(ai_message)
    print("AI\t:" + ai_message.content)
        
    
    