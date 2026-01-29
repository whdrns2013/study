from core.openai_api import chat_gpt
from tools.gpt_functions import tools

STREAM=True

def terminal_chat():
    messages = []
    while True:
        inp = input("user\t:")
        if inp == "exit":
            break
        messages.append({"role":"user", "content":inp})
        response = chat_gpt(messages=messages, tools=tools, stream=STREAM)
        for chunk in response:
            print(chunk)
        ai_message = response.choices[0].message.content
        messages.append({"role":"assistant", "content":ai_message})
        print(ai_message)