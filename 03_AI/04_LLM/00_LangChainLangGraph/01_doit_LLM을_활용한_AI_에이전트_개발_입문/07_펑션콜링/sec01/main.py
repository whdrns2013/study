from service.what_time_is_it_terminal import terminal_conversation
from core.streamlit_chat import streamlit_chat
from core.openai_api import chat_gpt

def main():
    # messages = [{"role" : "system", "content" : "너는 사용자를 도와주는 상담사야."},
    #             {"role" : "user", "content": "서울, 뉴욕, 도쿄의 시간은 몇시야?"}]
    # response = chat_gpt(messages=messages)
    # print(response)
    # terminal_conversation()
    streamlit_chat()


if __name__ == "__main__":
    main()
