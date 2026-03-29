import streamlit as st
from config.config import config
from core.openai_model import get_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

def get_ai_response(llm, messages, stream):
    if stream:
        # response = llm.stream(messages)
        # for chunk in response:
        #     yield chunk
        return llm.stream(messages)
    else:
        response = llm.invoke(messages)
        return response

def streamlit_chat(stream=config.getboolean("setting", "mode.stream")):
    
    # 사이드바 : 
    with st.sidebar:
        "Streamlit 테스트"
    
    # title
    st.title("🤖 Doit Chatbot")
    
    # 모델 선언
    llm = get_model()
    
    # 초기 메시지
    if "messages" not in st.session_state: # st.session_state : 스트림릿에서 사용자의 세션 상태 관리
        st.session_state.messages = [SystemMessage("당신은 사용자의 질문에 친절하게 답하는 AI 챗봇입니다.")]
        st.session_state.messages.append(AIMessage("안녕하세요! 무엇을 도와드릴까요?"))
    
    # 대화 기록을 웹브라우저에 출력
    for mgs in st.session_state.messages:
        if mgs:
            if (isinstance(mgs, SystemMessage)) and (config.getboolean("setting", "mode.debug")):
                st.chat_message("system").write(mgs.content)
            if isinstance(mgs, AIMessage):
                st.chat_message("assistant").write(mgs.content)
            if isinstance(mgs, HumanMessage):
                st.chat_message("user").write(mgs.content)
    
    # LLM 에 질의
    if prompt := st.chat_input(): # 사용자의 입력을 받아 prompt 변수에 할당
        user_message = HumanMessage(prompt)
        st.session_state.messages.append(user_message)
        st.chat_message("user").write(prompt)
        
        # 질의에 대한 응답 받아옴
        if stream:
            response_gen = get_ai_response(llm, st.session_state.messages, stream)
            result = st.chat_message("assistant").write_stream(response_gen) # write_stream 은 출력 + 문자열 반환
        else:
            response = get_ai_response(llm, st.session_state.messages, stream)
            result = response.content
            st.chat_message("assistant").write(result) # write : 출력만 함 (반환 없음)
        
        st.session_state.messages.append(AIMessage(result))
    
# streamlit 실행
# uv run streamlit run main.py
