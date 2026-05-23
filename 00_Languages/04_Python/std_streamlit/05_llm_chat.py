# 05_llm_chat.py
import streamlit as st
import random
import time

st.title("05. LLM Chat")
st.markdown("Streamlit은 LLM 채팅 화면을 빠르게 구현하는 도구로도 유명하다. 또한, 이미지나 데이터프레임과 같은 다양한 컨텐츠 유형도 지원한다!")

# 1. 채팅 히스토리 초기화  
# st.session_state : 세션 상태
if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant", "content":"안녕하세요? 어떻게 도와드릴까요?😀"}] # 세션 상태에 messages와 초기 메시지 할당

# 2. 앱 시작, 재시작시 메시지 출력  
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. 사용자의 입력을 받아옴  
if prompt := st.chat_input("기본 플레이스홀더"): # 챗 인풋을 받아서
    
    # (1) 세션에 저장
    st.session_state.messages.append({"role":"user", "content":prompt})
    
    # (2) 화면에 출력
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # (3) AI 답변 생성 및 출력
    with st.chat_message("assistant"):
        message_placeholder = st.empty() # 화면에 출력하는 문자열
        full_response = "" # 전체 답변 -> 답변 청크가 모두 끝나고 messages에 저장
        assistant_response = random.choice(
            [
                "안녕하세요? 어떻게 도와드릴까요?",
                "아 그러시군요! 잘 알겠어요.",
                "무슨 말씀인지 잘 모르겠어요."
            ]
        )
        
        for chunk in assistant_response.split(): # LLM Streaming 답변 재현
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response) # 입력바를 제외한 전체 완성 답변을 화면에 출력
    
    # (4) messages에 AI 생성 답변 저장
    st.session_state.messages.append({"role":"assistant", "content":full_response})
