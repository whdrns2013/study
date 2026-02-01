

## 랭체인  

### 소개  

- 랭체인 (LangChain)  
- 언어 모델에 기반한 AI 애플리케이션을 쉽게 개발할 수 있도록 도와주는 "프레임워크"  
- 이러한 프레임워크를 사용하지 않는다면 원하는 모든 기능을 직접 구현해야 하지만  
- 랭체인과 같은 프레임워크를 사용한다면 어떤 문제 해결을 위해 이미 구현된 다양한 도구와 모듈들을 가져와 사용하기만 하면 됨  
- 또한 작업의 체계 등에서도 도움을 받을 수 있어  
- 복잡한 애플리케이션을 개발할 때도 미리 구축된 모듈과 체계를 이용해 개발 속도를 높일 수 있다.  
- 또한 랭체인은 서로 다른 여러 언어 모델을 쉽게 교체하며 사용할 수 있다.  

> 프레임워크  
> 어떠한 목적을 달성하기 위해 복잡하게 얽혀있는 문제를 해결하기 위한 구조  
> 소프트웨어 개발에 있어 하나의 뼈대 역할을 한다.  

### 설치  

```bash
# 랭체인
pip install langchain

# 랭체인 OpenAI
pip install langchain-openai
```

- langchain 은 LLM 애플리케이션을 만들기 위한 본체 (Core Framework)  
- langchain-openai 는 OpenAI 모델을 langchain 에 연결시켜 주는 플러그인 같은 존재    


### Integration  

- Langchain 의 기능을 외부 시스템이나 서비스와 연동하도록 해주는 모듈 또는 패키지  
- Langchain 의 ecosystem 에는 이러한 langchain-openai 와 같은 것들, 외부의 LLM 모델이나 API 와 연동하는 것들이 있는데  
- LangChain에서는 외부 LLM, 벡터스토어, 툴, API 등을 연결하는 것을 Integration이라고 부흔다.  
- 이러한 연결을 가능하게 하는 패키지를 Integration Package라고 지칭한다.  
- 또한 Integration 대상이 되는 외부 업체 또는 서비스를 Provider라고 부흔다.  
- 따라서 그 외에 도 아래와 같은 여러 Integration 패키지들이 있다.  

```bash
pip install langchain-google-vertexai
pip install langchain-anthropic
pip install langchain-aws
pip install langchain-google-genai
pip install langchain-ollama
pip install langchain-groq
pip install langchain-huggingface

# LLM 서비스만 있는 게 아니다  
pip install langchain-postgres
pip install langchain-mongodb
```

- 어떤 integration packages 가 있는지는 아래 페이지에서 확인할 수 있따.  

https://docs.langchain.com/oss/python/integrations/providers/overview


### 사용법  

#### API 키 설정  

- 환경변수에 API 키를 등록해놓을 수 있다.  
- 예) `OPENAI_API_KEY` 환경변수에 API key를 등록해놓으면 필요시 해당 값을 불러들여 사용한다.  
- 또한 해당 프로젝트의(?) env 파일에 API 키가 기록되어있다면 생략할 수 있따.  

```python
import os
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
```

#### 모델 선언  

- Integration Package 에 따라 사용하면 된다.  
- 예를 들어 openai 의 모델은 `langchain_openai.ChatOpenAI` 의 인스턴스를 생성한다.  

```python
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o-mini")
```

#### 메시지  

- 메시지 객체는 `langchain_core` 의 `message` 모듈 안에 정의되어있다.  
- 사용자의 메시지는 `HumanMessage` 클래스  
- AI의 응답 메시지는 `AIMessage` 클래스  
- system 메시지는 `SystemMessage` 클래스를 이용한다.  
- 앞으로 이들을 통틀어 Message 클래스라고 지칭한다..  

#### LLM 에 메시지 보내기  

- model 인스턴스의 `invoke` 메서드를 이용해 메시지를 보낼 수 있다.  
- invoke 메서드에 인자로 `list[Message]` 형태의 자료를 담아 보내면 된다.  

```python
# API 키
os.environ["OPENAI_API_KEY"] = config.get("apikey", "openai")

# 모델 선언
model = ChatOpenAI(model="gpt-4o-mini")

# Message
messages = []
messages.append(HumanMessage(content="안녕? 내 이름은 Jongya야."))

# 메시지 보내기
response = model.invoke(messages)
print(response)
```

```bash
content='안녕하세요, Jongya! 만나서 반가워요. 어떻게 도와드릴까요?'
additional_kwargs={'refusal': None}
response_metadata={'token_usage': .... }
```

### 멀티턴 대화하기  

#### 기본적인 멀티턴 구축 개념  

- langchain 에서 멀티턴 대화를 구축하는 방법은 기본적으로 같다.  
- 메시지들을 담은 리스트에 사용자의 질문과 LLM의 답변을 계속 추가해나가면 된다.  

```python
import os
from config.config import config
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["OPENAI_API_KEY"] = config.get("apikey", "openai")
messages = [SystemMessage(content="너는 사용자를 도와주는 상담사야")]
model = ChatOpenAI(model="gpt-4o-mini")

while True:
    inp = input("user\t:")
    if input == "exit":
        break
    
    messages.append(HumanMessage(content=inp))       
    response = model.invoke(messages)
    print("AI\t:" + response.content)
```


```bash
user    :안녕? 나는 Jongya야.
AI      :안녕, Jongya! 만나서 반가워. 어떻게 도와줄 수 있을까?
user    :내 이름이 뭐라고?
AI      :안녕하세요, Jongya님! 당신의 이름을 잘 기억하고 있습니다. 어떻게 도와드릴까요?
```

### 메시지 히스토리를 이용한 멀티턴 구현  

#### 랭체인 메시지 히스토리  

- 앞선 예시에서는 멀티턴 구축을 위해 매번 사용자의 메시지와 LLM의 메시지를 리스트나 딕셔너리에 추가해야 했음  
- 하지만 랭체인의 메시지 히스토리 기능을 사용하면 멀티턴 대화를 더 쉽게 구현할 수 있음  
- `langchain_core.chat_history` 모듈의 `InMemoryChatMessageHistory` 클래스 : 메모리 내에서 메시지를 리스트 형태로 보관하는 것. 애플리케이션을 종료하면 대화 내용이 사라진다. 따라서 대화 내역을 계속 보관하고 싶다면 파일이나 DB에 저장해야 한다.    
- `langchain_core.runnables.history` 모듈의 `RunnableWithMessageHistory` 클래스 :  모델을 생성할 때 대화 기록을 함께 전달할 수 있게 해주는 클래스    

#### 대화 세션  

- 세션 : 두 개 이상의 통신 장치에서 끝점(클라이언트-서버, 또는 클-클, 서-서)간의 대화식 표현 및 정보 교환을 가능케 하기 위해 상태를 저장하는 개념, 또는 그게 이뤄지는 계층  
- 대화 세션은, 특정한 대화의 상태와 이력을 저장하는 개념을 의미한다.  
- 여기서 대화 세션은, 특정한 대화의 흐름을 의미하며, 한 대화 세션(예를들어 세션 id 123)은 다른 대화 세션(id 456)과 혼합되지 않는다.  

![alt text](/assets/images/store.png)


#### 대화 세션 저장소와 세션 히스토리 반환 함수 만들기  

- store : 대화 세션을 저장하는 저장소  
- session_id : 대화 세션을 식별하는 식별자  

```python
import os
from config.config import config
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

def get_model():
    os.environ["OPENAI_API_KEY"] = config.get("apikey", "openai")
    model = ChatOpenAI(model="gpt-4o-mini")
    return model

store = {} # 대화 내역을 저장할 store

def get_session_history(session_id:str) -> BaseChatMessageHistory: # session_id : 대화 세션을 반환받고자 하는 세션의 식별자
    # 만약 session store에 없는 session_id 라면
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory() # 메모리에 있는 대화 기록을 저장하는 객체 생성
    return store[session_id] # 해당 세션의 대화 기록을 반환하도록 함
```

- 구조를 보면, store는 dictionary 형태의 저장소 역할을 하게 된다.  
- 이 store에 저장되는 내용물은 `store[session_id]` 부분을 보면 알 수 있듯, session_id 를 키로 하며  
- value는 InMemoryChatMessageHistory() 객체를 할당한다.  
- 반환값의 타입 힌트로 사용되는 BaseChatMessageHistory 클래스는 기본적인 MessageHistory 클래스의 추상 베이스 클래스(인터페이스 성격)다.    

#### InMemoryChatMessageHistory - 대화 세션의 상태를 기록하는  

- 이 흐름으로 봤을 때 InMemoryChatMessageHistory 는 "대화의 세션"에 귀속된 대화 기록 객체라고 보면 좋다.    

```plaintext
session_id (세션 식별자)
   ↓
store (세션 저장소)
   ↓
InMemoryChatMessageHistory (해당 세션의 대화 기록)
```

#### RunnableWithMessageHistory - 히스토리를 사용하며 사용자와 인터랙션 할 래퍼 클래스  

- 앞서 소개한 두 가지 History로 끝나는 클래스 중 하나  
- 이 Runnable... 은 앞서 소개한 InMemory... 같은 와는 달리 히스토리를 저장하는 History 클래스가 아니다.  
- Runnable wrapper 클래스이고, 히스토리를 참고하여, 사용자와 대화 인터랙션을 담당하는 클래스이다.  
- 둘 모두 이름이 History 로 끝나서 헷갈릴 수 있지만, 헷갈리지 말도록 하자.  

> InMeMoryChatMessageHistory : BaseChatMessageHistory 계열  
> RunnableWithMessageHistory : Runnable + History 를 결합하는 어댑터 역할  


- 이 클래스가 받는 인자는 아래와 같다.  

```python
class RunnableWithMessageHistory(
    runnable: Runnable[list[BaseMessage], MessagesOrDictWithMessages | str | BaseMessage] | Runnable[dict[str, Any], MessagesOrDictWithMessages | str | BaseMessage] | LanguageModelLike,
    get_session_history: GetSessionHistoryCallable,
    *,
    input_messages_key: str | None = None,
    output_messages_key: str | None = None,
    history_messages_key: str | None = None,
    history_factory_config: Sequence[ConfigurableFieldSpec] | None = None,
    **kwargs: Any
)
```

- 대표적인 인자만 살펴보자면 아래와 같다.  

1. runnable : 실제로 LLM 호출 또는 체인 실행을 담당하는 본체 로직이다. 하지만 "History를 모르는 상태"이다.  
ChatOpenAI 클래스 또한 Runnable 의 일종으로 볼 수 있다.  

```plaintext
Runnable (프로토콜/개념)
  ↑
BaseLanguageModel
  ↑
BaseChatModel
  ↑
ChatOpenAI
```

2. get_session_history : 세션 ID를 받고, BaseChatMessageHistory 객체를 반환하는 팩토리 함수  

3. 그래서 RunnableWithMessageHistory는  
실제로 LLM을 호출하고 사용자와 인터랙션을 하지만 History는 모르는 Runnable 객체 + History를 공급해주는 get_session_history  
이 둘을 wrapping 하여 History를 알면서 인터랙션할 수 있게 해준다.  

--> 이 부분이 이해하는 데 가장 오래 걸림  

![alt text](/assets/images/runnable_with_message_history.png)

#### Runnable... 과 InMemory... 를 이용한 멀티턴 구축  

```python
import os
from config.config import config
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

def get_model():
    os.environ["OPENAI_API_KEY"] = config.get("apikey", "openai")
    model = ChatOpenAI(model="gpt-4o-mini")
    return model

store = {} # 대화 내역을 저장할 store

def get_session_history(session_id:str) -> BaseChatMessageHistory: # session_id : 대화 이력을 반환받고자 하는 세션의 식별자
    # 만약 session store에 없는 session_id 라면
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory() # 메모리에 있는 대화 기록을 저장하는 객체 생성
    return store[session_id] # 해당 세션의 대화 기록을 반환하도록 함

model = get_model()
with_message_history = RunnableWithMessageHistory(model, get_session_history) # --- 대화 내용을 저장하면서 대화를 이어나가는 클래스
```

#### 실습 해보기  

- 이제 실습을 해본다. 사용자의 메시지를 입력해서 LLM의 응답을 받기 위해서는 동일하게 `invoke` 메서드를 사용한다.  

- 먼저 "abc2" 라는 세션에 대화를 기록해보도록 한다.  

```python
config = {"configurable": {"session_id":"abc2"}}

response = with_message_history.invoke(
    [HumanMessage(content="안녕? 나는 Jongya야.")],
    config = config
)

print(response.content)
```

```bash
안녕, Jongya! 만나서 반가워. 어떻게 도와줄까요?
```

- 대화의 맥락을 기억하는지 내 이름을 다시 물어본다.  

```python
response = with_message_history.invoke(
    [HumanMessage(content="내 이름이 뭐라고?")],
    config = config
)

print(response.content)
```

```bash
당신의 이름은 Jongya입니다. 맞나요?
```

- 이제 세션 id 를 바꾸고, 맥락을 기억하는지 테스트해본다.  

```python
# 세션 아이디를 바꾸면 이전 대화내용을 모름  
config = {
    "configurable" : {"session_id":"aaa1"}
}

response = with_message_history.invoke(
    [HumanMessage(content="내 이름이 뭐라고?")],
    config = config
)

print(response.content)
```

```bash
죄송하지만, 당신의 이름을 알 수 있는 정보가 없습니다. 이름을 알려주시면 좋겠습니다!
```

#### store 살펴보기  

- 대화 세션들을 저장하는 store가 어떻게 쌓이고 있는지 출력해보자  

```python
# store를 출력해보면  
from pprint import pprint
pprint(store)
```

```bash
{'abc2':
    InMemoryChatMessageHistory(
        messages=[
            HumanMessage(content='안녕? 나는 Jongya야.', additional_kwargs={}, response_metadata={}),
            AIMessage(content='안녕하세요, Jongya! 어떻게 도와드릴까요?', additional_kwargs={'refusal': None}},
            HumanMessage(content='내 이름이 뭐라고?', additional_kwargs={}, response_metadata={}),
            AIMessage(content='당신의 이름은 Jongya입니다. 맞나요?', additional_kwargs={'refusal': None}...,
 'ccc1':
    InMemoryChatMessageHistory(
        messages=[
            HumanMessage(content='내 이름이 뭐라고?', additional_kwargs={}, response_metadata={}),
            AIMessage(content='죄송하지만, 당신의 이름은 알 수 없습니다. 하지만 당신과의 대화에서 도와드릴 수 있는 것이 있으면 말씀해 주세요!', ...
}
```

### Stream 방식 출력

- stream 방식으로 출력을 하기 위해서는 `invoke` 메서드 대신 `stream` 메서드를 사용하면 된다.  

```python
config = {"configurable": {"session_id":"abc2"}}

for r in with_message_history.stream(
    [HumanMessage(content="내가 어느 나라 사람인지 맞춰보고, 그 나라의 국가를 불러줘.")],
    config = config):
    print(r.content, end="|")
```

```bash
|이|름|을| 기준|으로| 추|측|해| 보|건|대|,| "|J|ong|ya|"|는| 한국|에서| 비롯|된| 이름|일| 가능|성이| 높|습니다|.| 그렇|다면| 한국|의| 국가|인| "|애|국|가|"|를| 불|러|드|리|겠습니다|.| 
|애|국|가|의| 일부|는| 다음|과| 같습니다|:
|"|동|해| 물|과| 백|두|산|이| 마|르고| 닳|도록|..."
|만|약| 다른| 나라|의| 사람|이라|면|,| 어떤| 나라|인지| 말씀|해| 주|시면| 그|에| 맞|는| 국가|를| 알려|드|릴| 수| 있습니다|!||||
```

- 어떻게 한국사람 이름이 Jongya...  


## Reference  

https://namu.wiki/w/%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC  
https://ko.wikipedia.org/wiki/%EC%84%B8%EC%85%98_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99)

