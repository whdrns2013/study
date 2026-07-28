import streamlit as st
from config.config import config
from core.openai_model import get_model
from tools.generate_chat_id import generate_chat_id
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

def get_session_history(session_id:str) -> BaseChatMessageHistory:
    if session_id not in st.session_state["store"]:
        st.session_state["store"][session_id] = InMemoryChatMessageHistory()
    return st.session_state["store"][session_id]

def streamlit_chat(stream=config.getboolean("setting", "mode.stream")):
    
    # 사이드바 : 
    with st.sidebar:
        "Streamlit 테스트"
    
    # title
    st.title("🤖 Doit Chatbot")
    
    # 초기 메시지
    if "messages" not in st.session_state: # st.session_state : 스트림릿에서 사용자의 세션 상태 관리
        st.session_state.messages = [SystemMessage("당신은 사용자의 질문에 친절하게 답하는 AI 챗봇입니다.")]
        st.session_state.messages.append(AIMessage("안녕하세요! 무엇을 도와드릴까요?"))
    
    # 대화 세션 스토어 생성
    if "store" not in st.session_state:
        st.session_state["store"] = {}
    
    llm = get_model()
    with_message_history = RunnableWithMessageHistory(llm, get_session_history)
    
    # 세션 스토어에서 현재 세션id를 찾고, 없으면 생성
    session_id = ""
    if "session_id" not in st.session_state:
        session_id = generate_chat_id()
        st.session_state["session_id"] = session_id
    model_config = {"configurable":{"session_id":session_id}}
    
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
        response = None
        content = None
        if stream:
            response_chunk = with_message_history.stream(user_message, config=model_config)
            response = None
            with st.chat_message("assistant").empty():
                for r in response_chunk:
                    if response is None:
                        response = r
                    else:
                        response += r
                    st.markdown(response.content)
            content = response.content
        else:
            response = with_message_history.invoke(user_message, config=model_config)
            content = response.content
            st.chat_message("assistant").write(content)
        st.session_state.messages.append(response)
        st.session_state.messages.append({"role":"assistant", "content":content})
    
# streamlit 실행
# uv run streamlit run main.py
