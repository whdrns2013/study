import streamlit as st
from config.config import config
from core.openai_model import get_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
from tools.langchain_tools import tools, tool_dict

def streamlit_chat(stream=config.getboolean("setting", "mode.stream")):
    
    # 사이드바 : 
    with st.sidebar:
        "Streamlit 테스트"
    
    # title
    st.title("🤖 Doit Chatbot")
    
    # 모델 선언
    llm = get_model()
    llm_with_tools = llm.bind_tools(tools)
    
    # 초기 메시지
    if "messages" not in st.session_state: # st.session_state : 스트림릿에서 사용자의 세션 상태 관리
        st.session_state.messages = [SystemMessage("당신은 사용자의 질문에 친절하게 답하는 AI 챗봇입니다.")]
        st.session_state.messages.append(AIMessage("안녕하세요! 무엇을 도와드릴까요?"))
    
    # 대화 기록을 웹브라우저에 출력
    for msg in st.session_state.messages:
        if msg:
            if (isinstance(msg, SystemMessage)) and (config.getboolean("setting", "mode.debug")):
                st.chat_message("system").write(msg.content)
                st.chat_message("tool").write(msg.content)
            if isinstance(msg, AIMessage):
                st.chat_message("assistant").write(msg.content)
            if isinstance(msg, HumanMessage):
                st.chat_message("user").write(msg.content)
    
    # LLM 에 질의
    if prompt := st.chat_input(): # 사용자의 입력을 받아 prompt 변수에 할당
        user_message = HumanMessage(prompt)
        st.session_state.messages.append(user_message)
        st.chat_message("user").write(prompt)
        
        # 질의에 대한 응답 받아옴
        if stream:
            # 사용자 질문에 대한 응답
            response = llm_with_tools.stream(st.session_state.messages)

            # garhering
            gathered = None

            def stream_gen():
                nonlocal gathered
                for chunk in response:
                    # chunk 누적
                    if gathered is None:
                        gathered = chunk
                    else:
                        gathered += chunk
                    yield chunk.content or ""

            # ⚠️ 출력하지 않고 수집만
            _ = list(stream_gen())

            # gathered == AIMessage
            if (gathered is not None):
                st.session_state.messages.append(gathered)
            
            # tool 처리
            if gathered and gathered.tool_calls:
                for tool_call in gathered.tool_calls:
                    tool = tool_dict[tool_call["name"]]
                    tool_msg = tool.invoke(tool_call)
                    st.session_state.messages.append(tool_msg)
                
                # tool 결과 반영 응답
                final_response = llm_with_tools.stream(st.session_state.messages)
                final_gathered = None

                def final_stream_gen():
                    nonlocal final_gathered
                    for chunk in final_response:
                        if final_gathered is None:
                            final_gathered = chunk
                        else:
                            final_gathered += chunk
                        yield chunk.content or ""

                result = st.chat_message("assistant").write_stream(final_stream_gen())
                st.session_state.messages.append(final_gathered)

            else:
                if gathered:
                    st.chat_message("assistant").write(gathered.content)
            
        else:
            response = llm_with_tools.invoke(st.session_state.messages)
            result = response.content
            st.chat_message("assistant").write(result) # write : 출력만 함 (반환 없음)
            st.session_state.messages.append(response)
        
    
# streamlit 실행
# uv run streamlit run main.py
