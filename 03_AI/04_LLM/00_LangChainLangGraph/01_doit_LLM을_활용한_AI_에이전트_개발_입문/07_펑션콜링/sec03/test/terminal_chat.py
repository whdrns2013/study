from core.openai_api import chat_gpt
from tools.gpt_functions import tools
from config.config import config

def terminal_chat(stream=False):
    messages = []
    while True:
        inp = input("user\t:")
        if inp == "exit":
            break
        messages.append({"role":"user", "content":inp})
        response, tool_calls = chat_gpt(messages=messages, tools=tools, stream=stream)
        if stream:
            content = ""
            for chunk in response:
                if hasattr(chunk, "choices"):
                    content_chunk = chunk.choices[0].delta.content
                    if content_chunk:
                        print(content_chunk, end="", flush=True) # print 가 출력 버퍼를 채우느라 뭉쳐서 나오는 경우가 있음 -> 강제로 바로 출력하도록 함
                        content += content_chunk
                    else:
                        print("\n")
            ai_message = content
        else:
            ai_message = response.choices[0].message.content
            print(ai_message)
        messages.append({"role":"assistant", "content":ai_message})