import streamlit as st
from config.config import config
from tools.generate_chat_id import generate_chat_id

def streamlit_chat(chat_wrapper,
                   default_messages=[{"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}],
                   stream=False):
    
    # 사이드바 : 
    with st.sidebar:
        "Streamlit 테스트"
    
    # title
    st.title("🤖 Doit Chatbot")
    
    # 초기 메시지
    if "messages" not in st.session_state: # st.session_state : 스트림릿에서 사용자의 세션 상태 관리
                                           # 사용자가 웹 브라우저에서 상호작용하는 동안 상태가 저장/유지되고 업데이트 됨
        st.session_state.messages = default_messages # 세션이 없으면 초기 메시지 보여줌
    
    # 대화 세션 스토어 생성
    if "store" not in st.session_state:
        st.session_state["store"] = {}
    
    # 세션 스토어에서 현재 세션id를 찾고, 없으면 생성
    if "session_id" not in st.session_state:
        session_id = generate_chat_id()
        st.session_state["session_id"] = session_id
    model_config = {"configurable":{"session_id":session_id}}
    
    # 멀티턴 모델 래퍼 가져오기
    chat_function = chat_wrapper.get_with_message_history(st.session_state["store"], st.session_state["session_id"])
    
    # 대화 기록을 웹브라우저에 출력
    for message in st.session_state.messages:
        if config["setting"]["mode.debug"] == "1": # debug 모드인 경우 모든 메시지 출력
            expose_message = True
        else: # debug 모드가 아닌 경우 유저 입력과 LLM 답변만 출력
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
        response, tool_calls = chat_function(messages = st.session_state.messages, stream = stream)
        content = ""
        if stream:
            with st.chat_message("assistant").empty():
                for chunk in response:
                    content_chunk = chunk.choices[0].delta.content
                    if content_chunk:
                        content += content_chunk
                        st.markdown(content)
        else:
            # 화면에 응답 출력
            with st.chat_message("assistant"):
                content = response.choices[0].message.content
                st.markdown(content)
        # tool_calls 를 화면에 출력
        if len(tool_calls) > 0:
            tool_call_msg = [tool_call["function"] for tool_call in tool_calls]
            with st.expander("tool calls", expanded=False):
                st.write(tool_call_msg)
        # 응답을 세션에 업데이트
        st.session_state.messages.append({"role":"assistant", "content":content})
    
# streamlit 실행
# uv run streamlit run main.py
