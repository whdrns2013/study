import streamlit as st
from core.openai_api import chat_gpt
from config.config import config

def streamlit_chat(chat_function=chat_gpt):
    
    # 사이드바 : 
    with st.sidebar:
        "Streamlit 테스트"
    
    # title
    st.title("🤖 Doit Chatbot")
    
    # 초기 메시지
    if "messages" not in st.session_state: # st.session_state : 스트림릿에서 사용자의 세션 상태 관리
                                           # 사용자가 웹 브라우저에서 상호작용하는 동안 상태가 저장/유지되고 업데이트 됨
        st.session_state.messages = [{"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}] # 세션이 없으면 초기 메시지 보여줌
    
    # 대화 기록을 웹브라우저에 출력
    for message in st.session_state.messages:
        if config["setting"]["mode.debug"] == "1":
            expose_message = True
        else:
            expose_message = (message["role"] == "user") or (message["role"] == "assistant")
        if expose_message:
            with st.chat_message(message["role"]): # st.chat_message : 스트림릿의 채팅 인터페이스에 메시지를 출력하는 용도 (assistant / user)
                st.markdown(message["content"])    # st.markdown : 컨텐츠를 출력할 형태 지정 - 마크다운으로 (기본은 write)
    
    # LLM 에 질의
    if prompt := st.chat_input(): # 사용자의 입력을 받아 prompt 변수에 할당
        st.session_state.messages.append({"role": "user", "content": prompt}) # 사용자의 질문을 상태 - 메세지에 추가
        with st.chat_message("user"): # 사용자의 질문을 화면의 "chat message container"로 보여줌
            st.markdown(prompt)
        # 질의에 대한 응답 받아옴
        response = chat_function(messages = st.session_state.messages)
        msg = response.choices[0].message.content
        # 응답을 세션에 업데이트
        st.session_state.messages.append({"role":"assistant", "content":msg})
        # 화면에 응답 출력
        with st.chat_message("assistant"):
            st.markdown(msg)
    
    # TODO: 스트리밍 적용
    

# streamlit 실행
# uv run streamlit run main.py
