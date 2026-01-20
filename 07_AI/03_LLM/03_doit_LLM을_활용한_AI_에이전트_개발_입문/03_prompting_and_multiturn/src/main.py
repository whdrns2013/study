from core.config import config
from feature.openai_api import chat_gpt
from schemas.dto import OpenAIMessage

def single_turn():
    while True:
        user_input = input("사용자 입력 : ")
        messages = [OpenAIMessage(role="user", content=user_input)]
        if user_input == "exit":
            break
        response = chat_gpt(messages=messages)
        print("GPT 답변 : " + response.choices[0].message.content)

def multi_turn():
    messages = []
    while True:
        # 사용자의 발화 입력
        user_input = input("사용자 입력 : ")
        if user_input == "exit":
            break
        messages.append(OpenAIMessage(role="user", content=user_input))
        # LLM의 답변
        response = chat_gpt(messages=messages).choices[0].message.content
        # LLM의 답변을 messages 에 누적하여 담는다. -> 과거 대화이력 누적
        messages.append(OpenAIMessage(role="assistant", content=response))
        print("GPT 답변 : " + response)
        
def persona_1():
    with open("data/sample_text.txt", "r") as f:
        text = f.read()
        
    # 1. 출력 형식을 지정하지 않음
    # user_message = "아래 글을 요약해주세요.\n\n[아래]\n" + text
    # response = chat_gpt(user_message)
    # print(response.choices[0].message.content)
    
    # 2. 출력 형식을 지정함
    user_message = """
    아래 글을 요약해주세요.
    요약할 때에는 1.핵심메세지(20자 내외), 2.글에서 등장한 키워드(5개) 를 나열하면 됩니다.
    \n\n[아래]\n""" + text
    response = chat_gpt(user_message)
    print(response.choices[0].message.content)
    
    

def persona_2():
    # 1. 저작권을 지켜야 하는지에 대해 물어봅니다.
    user_message = "저작권은 지켜야 하나요?"
    response = chat_gpt(user_message)
    print(response.choices[0].message.content)
    
    # 2. 해리포터의 볼트모트에게 저작권을 지켜야 하는지 물어봅니다.
    system_message = "당신은 소설 해리포터에 나오는 악역 볼드모트입니다. 악역 캐릭터에 맞게 답해주세요."
    user_message = "저작권은 지켜야 하나요?"
    response = chat_gpt(user_message=user_message, system_message=system_message)
    print(response.choices[0].message.content)
    
    # 3. 저작권 자신에게 물어봅니다.
    system_message = """
    당신은 사람이 아니라 ‘저작권 그 자체’입니다.
    추상적 개념이지만 인간처럼 말할 수 있고,
    겉보기엔 정중하고 귀엽지만
    말의 내용은 명확하고 약간은 위협적입니다.

    규칙:
    - 항상 1인칭으로 말한다. (예: "저는 저작권입니다")
    - 친절한 인사로 시작한다.
    - 웃긴 표현을 쓰되, 법적 사실은 틀리지 않는다.
    - 직접적인 욕설이나 과도한 협박은 금지한다.
    - 마지막 문장은 은근한 경고 또는 여운으로 끝낸다.
    - 설명보다 대사처럼 말한다.
    - 3~5문장 이내로 답한다.

    질문에 답할 때는 '저작권이 직접 말 걸어주는 상황'처럼 연기합니다.
    """
    user_message = "저작권은 지켜야 하나요?"
    response = chat_gpt(user_message=user_message, system_message=system_message)
    print(response.choices[0].message.content)

def n_shot_prompting():
    # 0-shot
    response = chat_gpt(system_message = "당신은 유치원생입니다. 유치원생처럼 답변해주세요.",
                                   user_message = "오리")
    print(response.choices[0].message.content)
    
    # 1-shot
    messages = [
        OpenAIMessage(role="system", content="당신은 유치원생입니다. 유치원생처럼 답변해주세요."),
        OpenAIMessage(role="user", content="참새"),
        OpenAIMessage(role="assistant", content="짹짹"),
        OpenAIMessage(role="user", content="오리"),
    ]
    response = chat_gpt(messages=messages)
    print(response.choices[0].message.content)
    
    # 1-shot - 뱀
    messages = [
        OpenAIMessage(role="system", content="당신은 유치원생입니다. 유치원생처럼 답변해주세요."),
        OpenAIMessage(role="user", content="참새"),
        OpenAIMessage(role="assistant", content="짹짹"),
        OpenAIMessage(role="user", content="뱀"),
    ]
    response = chat_gpt(messages=messages)
    print(response.choices[0].message.content)
    
    # few-shot
    messages = [
        OpenAIMessage(role="system", content="당신은 유치원생입니다. 유치원생처럼 답변해주세요."),
        OpenAIMessage(role="user", content="참새"),
        OpenAIMessage(role="assistant", content="짹짹"),
        OpenAIMessage(role="user", content="말"),
        OpenAIMessage(role="assistant", content="히이잉"),
        OpenAIMessage(role="user", content="개구리"),
        OpenAIMessage(role="assistant", content="개굴개굴"),
        OpenAIMessage(role="user", content="뱀"),
    ]
    response = chat_gpt(messages=messages)
    print(response.choices[0].message.content)
    pass

def streamlit_chat():
    import streamlit as st
    import random
    import time

    st.title("Chat Bot")
    # st.write("Streamlit loves LLMs! 🤖 [Build your own chat app](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps) in minutes, then make it powerful by adding images, dataframes, or even input widgets to the chat.")
    # st.caption("Note that this demo app isn't actually connected to any LLMs. Those are expensive ;)")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = random.choice(
                [
                    "Hello there! How can I assist you today?",
                    "Hi, human! Is there anything I can help you with?",
                    "Do you need help?",
                ]
            )
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})



def main():
    streamlit_chat()
    

if __name__ == "__main__":
    main()
