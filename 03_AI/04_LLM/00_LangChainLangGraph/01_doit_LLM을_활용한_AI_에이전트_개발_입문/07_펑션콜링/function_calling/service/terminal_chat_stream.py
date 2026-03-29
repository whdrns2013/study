# terminal_chat.py
from openai import OpenAI
from tools.gpt_functions import tools, tool_mapping
from utils.tool_list_to_tool_obj import tool_list_to_tool_obj
from config.config import config
import json


def get_ai_response(messages:list[dict],
                    model:str="gpt-4o",
                    tools=tools,
                    api_key:str=config.get("apikey", "openai"),
                    stream=True):
    client = OpenAI(api_key = api_key)
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        tools = tools,
        stream = stream
    )
    return response

def terminal_chat_stream(stream=True):
    messages = []
    while True:
        # 사용자 입력
        user_input = input("◆ user\t:")
        if user_input == "exit":
            break
        
        # 대화 내역 추가
        messages.append({"role":"user", "content":user_input})
        
        # AI의 1차 답변
        response = get_ai_response(messages=messages, stream=stream)
        
        # AI 1차 답변 분석 및 처리
        ai_message = None
        if stream:
            ai_message = ""
            tool_calls_chunk = []
            print("◆ AI\t:", end='')
            for chunk in response: # 응답 안의 ChatCompletionChunk
                if hasattr(chunk, "choices"):
                    content_chunk = chunk.choices[0].delta.content # delta의 content
                    if content_chunk:
                        print(content_chunk, end='', flush=True) # 생성된 토큰씩 출력
                        ai_message += content_chunk
                    # 응답 안의 chunk 에서 tool_call 내용 수집
                    tool_delta = chunk.choices[0].delta
                    if hasattr(tool_delta, "tool_calls") and tool_delta.tool_calls:
                        tool_calls_chunk += tool_delta.tool_calls
            
            # 펑션 콜링이 있는 경우
            if tool_calls_chunk:
                ai_message = ""
                tool_obj = tool_list_to_tool_obj(tool_calls_chunk) # tool call 내용을 펑션 콜링하기 편한 방식으로 변환
                messages.append({"role":"assistant", "content":None, "tool_calls":tool_obj["tool_calls"]})
                for tool_call in tool_obj["tool_calls"]:
                    tool_name = tool_call["function"]["name"]
                    tool_call_id = tool_call["id"]
                    arguments = json.loads(tool_call["function"]["arguments"])
                    func_result = tool_mapping(tool_name=tool_name, arguments=arguments)
                    messages.append({"role":"tool", "tool_call_id":tool_call_id, "name":tool_name, "content":str(func_result)})
                response = get_ai_response(messages=messages, stream=stream)
                for chunk in response: # 응답 안의 ChatCompletionChunk
                    if hasattr(chunk, "choices"):
                        content_chunk = chunk.choices[0].delta.content # delta의 content
                        if content_chunk:
                            print(content_chunk, end='', flush=True) # 생성된 토큰씩 출력
                            ai_message += content_chunk
            print("\n")
            
            # AI 응답을 적재
            messages.append({"role":"assistant", "content":ai_message})
        else:
            if hasattr(response, "choices"):
            
                # 펑션 콜링 처리
                if response.choices[0].message.tool_calls:
                    print(response)
                    ai_message_obj = response.choices[0].message
                    tool_calls = ai_message_obj.tool_calls
                    
                    # messages 에 tool calls 추가
                    messages.append(ai_message_obj)
                    
                    # 펑션 콜링 처리
                    for tool_call in tool_calls:
                        tool_name = tool_call.function.name
                        tool_call_id = tool_call.id
                        arguments = json.loads(tool_call.function.arguments)
                        func_result = tool_mapping(tool_name=tool_name, arguments=arguments)
                        messages.append({"role":"tool", "tool_call_id":tool_call_id, "name":tool_name, "content":str(func_result)})
                        
                    # 펑션콜링 결과를 반영한 AI 2차 답변
                    response = get_ai_response(messages=messages)
                    
                # AI 최종 응답
                ai_message = response.choices[0].message.content
                messages.append({"role":"assistant", "content":ai_message})
            
            # 화면 출력
            if ai_message:
                print("◆ AI\t:" + ai_message)
