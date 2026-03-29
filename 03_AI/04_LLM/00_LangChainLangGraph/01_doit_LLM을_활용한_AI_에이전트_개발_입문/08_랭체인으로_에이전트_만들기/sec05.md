
## 스트림릿에 구현하기   

### 랭체인 메모리에 기반한 멀리턴 챗봇 만들기  

```python
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
        st.session_state["messages"] = [SystemMessage("당신은 사용자의 질문에 친절하게 답하는 AI 챗봇입니다.")]
        st.session_state["messages"].append(AIMessage("안녕하세요! 무엇을 도와드릴까요?"))
    
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
```

#### 겹치지 않는 session id 만들기  

> 이거 원리 공부하기  
> 번외 05  

```python
import uuid

def generate_chat_id() -> str:
    return str(uuid.uuid4())
```

### 랭체인 메모리 없이 멀티턴 만들기  

- 이 말은 곧 직접 리스트, 데이터베이스 등을 이용해 히스토리를 관리한다는 뜻이다.  
- 기존의 langchain + streamlit 코드에서 수정을 한다.  

```python
import streamlit as st
from config.config import config
from core.openai_model import get_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
from tools.langchain_tools import tools, tool_dict

def get_ai_response(llm, messages, stream):
    if stream:
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
            response_gen = get_ai_response(llm, st.session_state.messages, stream)
            result = st.chat_message("assistant").write_stream(response_gen) # write_stream 은 출력 + 문자열 반환
        else:
            response = get_ai_response(llm, st.session_state.messages, stream)
            result = response.content
            st.chat_message("assistant").write(result) # write : 출력만 함 (반환 없음)
        
        st.session_state.messages.append(AIMessage(result))
    
# streamlit 실행
# uv run streamlit run main.py
```

### 도구를 추가하고 스트림 방식으로 출력하기  

