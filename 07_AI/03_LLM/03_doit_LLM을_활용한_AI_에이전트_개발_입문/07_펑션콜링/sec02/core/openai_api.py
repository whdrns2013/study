from openai import OpenAI
from config.config import config
from schemas.dto import OpenAIMessage
import json
from tools.gpt_functions import tools, tool_mapping

def get_ai_response(messages:list[dict],
                    model:str,
                    temperature:float,
                    tools=None):
    api_key = config["apikey"]["openai"]
    client = OpenAI(api_key = api_key)
    response = client.chat.completions.create(
        model = model,
        temperature = temperature,
        messages = messages,
        tools = tools
    )
    return response

def chat_gpt(user_message:str|None=None,
             system_message:str|None=None,
             assistant_message:str|None=None,
             messages:list[OpenAIMessage]|list[dict]|None=None,
             model:str="gpt-4o",
             temperature:float=0.1,
             tools=tools):
    
    # 메시지 제작
    if messages:
        for i, message in enumerate(messages):
            if isinstance(message, OpenAIMessage):
                messages[i] = message.__dict__
    else:
        messages = []
        if system_message:
            messages.append({"role":"system", "content":system_message})
        if user_message:
            messages.append({"role":"user", "content":user_message})
        if assistant_message:
            messages.append({"role":"assistant", "content":assistant_message})
    
    # AI 응답 반환
    response = get_ai_response(messages=messages,
                               model=model,
                               temperature=temperature,
                               tools=tools)
    
    # function calling 처리
    if response.choices[0].message.tool_calls:
        tool_calls = response.choices[0].message.tool_calls
        for tool_call in tool_calls:
            # LLM 응답에서 도구 정보 추출
            tool_name = tool_call.function.name
            tool_call_id = tool_call.id
            arguments = json.loads(tool_call.function.arguments) 
            
            # 도구마다 사용 함수 매칭해서 도구의 결과를 메시지로 생성
            messages = tool_mapping(messages = messages,
                                    tool_name = tool_name,
                                    tool_call_id = tool_call_id,
                                    arguments = arguments)
        
        # 한번 더 gpt 응답 호출, 이번엔 도구의 결과와 도구 호출 id를 포함함
        messages.append({"role":"system", "content":"이제 주어진 결과들을 바탕으로 답변하시오"})
        response = get_ai_response(messages, model=model, temperature=temperature, tools=tools)
        
    return response

# 결과 텍스트 출력
# response.choices[0].message.content

# TODO: 스트리밍 적용