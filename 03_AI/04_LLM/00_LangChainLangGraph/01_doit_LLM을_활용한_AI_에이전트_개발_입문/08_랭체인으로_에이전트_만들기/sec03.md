
## 랭체인 도구로 에이전트 만들기   

### 랭체인 도구  

- 이전 장에서 펑션 콜링에 대해 공부해봤었다.  
- 랭체인에서도 이와 비슷한 방법을 Tools(도구)라는 이름으로 제공하고 있다.  

### `@tool` 데코레이터를 이용해 랭체인에 함수 연결하기  

- 이전 장에서 만든 현재 시간 알려주는 챗봇을 랭체인으로 만들어본다.  
- `@tool` 데코레이터를 사용하면 함수를 도구로 변환해준다.  
- 즉, 이 데코레이터는 함수를 랭체인의 외부 도구로 등록해, 언어 모델이 함수를 호출하고 사용할 수 있게 해준다.  
- 함수에 대한 정보 : """ """로 표시된 설명(주석)에 함수의 기능과 입력 인자, 사용 방법을 알려 주는 문서화 문자열을 기재한다. (기존의 펑션 콜링에서 딕셔너리로 작성했던 정보)

```python
from langchain_core.tools import tool
from datetime import datetime
import pytz

@tool
def get_current_time(timezone:str, location:str) -> str:
    """ 현재 시각을 반환하는 함수

    Args:
        timezone (str): 타임존(예: 'Asia/Seoul'). 실제 존재해야 함
        location (str): 지역명. 타임존은 모든 지명에 대응되지 않으므로 이후 llm 답변 생성에 사용됨
    """
    tz = pytz.timezone(timezone)
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    location_and_local_time = f"{timezone} ({location}) 현재 시각 : {now}"
    return location_and_local_time
```

- 그리고 사용할 수 있는 도구를 리스트와 딕셔너리 형태로 만든다.  
- 리스트에는 사용할 수 있는 **함수**를 모두 추가하고,  
- 딕셔너리에는 **도구의 이름**을 키로, 그리고 해당 도구 이름에 대응되는 (리스트에 추가했던)**함수**를 value로 저장한다.  
- 이렇게 만든 리스트와 딕셔너리는 `.bind_tools()`라는 메서드를 사용해 **기존에 선언한 언어모델에 도구를 등록**할 수 있다.  

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os
from config.config import config

def get_model(model:str="gpt-4o-mini", api_key:str|None=None):
    if api_key is None:
        os.environ["OPENAI_API_KEY"] = config.get("apikey", "openai")
    model = ChatOpenAI(model=model)
    return model

# 모델 선언
model = get_model()

# 도구 리스트와 딕셔너리  
tools = [get_current_time, ]
tool_dict = {"get_current_time": get_current_time, }

# 도구를 모델에 반영
llm_with_tools = model.bind_tools(tools)
```

이제 여기에 시간을 묻는 messages를 보내보면  

```python
# messages
messages = [
    SystemMessage("당신은 사용자의 질문에 답변하기 위해 tools를 사용할 수 있습니다."),
    HumanMessage("하와이와 부산은 지금 몇시잉교?")
]

# llm_with_tools 를 사용해 사용자 질문에 대한 답변 생성
response = llm_with_tools.invoke(messages)
messages.append(response)

# 생성된 답변 출력
print(messages)
```

```bash
[
    SystemMessage(
        content='당신은 사용자의 질문에 답변하기 위해 tools를 사용할 수 있습니다.',additional_kwargs={}, response_metadata={}
    ),
    HumanMessage(
        content='하와이와 부산은 지금 몇시잉교?', additional_kwargs={}, response_metadata={}
    ),
    AIMessage(
        content='', additional_kwargs={'refusal': None},...
        tool_calls=[
            {
                'name': 'get_current_time',
                'args': {'timezone': 'Pacific/Honolulu', 'location': 'Hawaii'},
                'id': 'call_**********', 'type': 'tool_call'
            },
            {
                'name': 'get_current_time',
                'args': {'timezone': 'Asia/Seoul', 'location': '부산'},
                'id': 'call_**********', 'type': 'tool_call'
            }
        ], ...
    )
]
```

생성된 답변을 보면 tool_calls 안에 두 개의 tool_call 이 있는 것을 확인할 수 있다.  
펑션콜링과 원리는 모두 같다. 이제 이들을 for 문으로 반복시켜 각각의 tool call 에 대한 결과물을 생성하고  
이 결과물을 다시 LLM 에게 보내 최종적인 답변을 하게 만들면 된다.  

```python
for tool_call in response.tool_calls:
    selected_tool = tool_dict[tool_call["name"]]
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)

messages
```

```bash
[
    SystemMessage(content='당신은 사용자의 질문에 답변하기 위해 tools를 사용할 수 있습니다.', additional_kwargs={}, response_metadata={}),
    HumanMessage(content='하와이와 부산은 지금 몇시잉교?', additional_kwargs={}, response_metadata={}),
    AIMessage(content='', ... tool_calls=[
        {'name': 'get_current_time', 'args': {'timezone': 'Pacific/Honolulu', 'location': '하와이'}},
        {'name': 'get_current_time', 'args': {'timezone': 'Asia/Seoul', 'location': '부산'}}
    ]),
    ToolMessage(content='Pacific/Honolulu (하와이) 현재 시각 : 2026-01-31 04:58:39', name='get_current_time', tool_call_id='call_***'),
    ToolMessage(content='Asia/Seoul (부산) 현재 시각 : 2026-01-31 23:58:39', name='get_current_time', tool_call_id='call_***')
]
```

여기에서 어떻게 selected_tool 에 invoke 메서드가 있을 수 있을까?  
그 해답은 바로, `@tool` 데코레이터가 일반 함수를 LangChain 에서 사용하는 표준화된 인터페이스를 가진 도구 객체로 업그레이드 해줬기 때문이다.  
이에 대한 자세한 탐구는 번외04에서 한다.  

이제 Tool 의 결과물 메시지까지 담긴 메시지들을 `llm_with_tools.invoke` 메서드에 넘기면 현재 시각 정보를 문장으로 답변해준다.  

```python

```

```bash
AIMessage(
    content='현재 하와이는 2026년 1월 31일 04:58:39이고, 부산은 2026년 1월 31일 23:58:39입니다.',
    ...
)
```

### Pydantic 이용하기  

- Pydantic : 입력 데이터의 유효성과 형식을 검증하고, 특정 데이터 형식으로 명확히 표현할 때 사용하는 라이브러리  
- dataclasses 가 클래스를 데이터 클래스로 명확하게 정의해주는 느낌이라면, Pydantic은 그것보다 더 넓은 범위를...  
- 즉, 객체지향 프로그래밍의 체계를 더해주는 느낌  
- 우선 Pydantic 으로 get_yf_stock_history 함수의 입력 포맷을 잡아보겠다.  

```python
from pydantic import BaseModel, Field

class StockHistoryInput(BaseModel):
    ticker: str = Field(..., title="주식 코드", description="주식 코드 (예:APPL)"),
    period: str = Field(..., title="기간", description="주식 데이터 조회 기간 (예: 1d, 1mo, 1y)")
```

- 그리고 다음으로 주식 이력을 조회하는 함수에 `@tool` 데코레이터를 더해 업그레이드 해준다.  

```python
@tool
def get_yf_stock_history(stock_history_input:StockHistoryInput):
    """ 주식 종목의 가격 데이터를 조회하는 함수 """
    stock = yf.Ticker(stock_history_input.ticker)
    hist = stock.history(stock_history_input.period)
    return str(hist.to_markdown())
```

- 앞서 했던 것처럼 tools 에 더해준 뒤, `.bind_tools` 메서드를 이용해 모델에 도구를 등록해준다.  

```python
tools = [get_current_time, get_yf_stock_history]
tool_dict = {
    "get_current_time":get_current_time,
    "get_yf_stock_history":get_yf_stock_history
}

llm_with_tools = model.bind_tools(tools)
```

- 이후 원하는 메시지를 작성한 뒤, 응답을 요청하고 툴을 처리한 뒤 최종 응답까지 요청한다.  

```python
# 메시지 작성
messages.append(HumanMessage("삼성전자의 주식은 한달 전에 비해 올랐어? 내렸어?"))

# 응답 요청
response = llm_with_tools.invoke(messages)
messages.append(response)

# 응답에 오는 툴 콜을 처리
for tool_call in response.tool_calls:
    selected_tool = tool_dict[tool_call["name"]]
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)

print(tool_msg)
```

```bash
ToolMessage(content='
| Date       | Open   | High   | Low    | Close  | Volume     | Dividends | Stock Splits |
|:-----------|-------:|-------:|-------:|-------:|-----------:|----------:|-------------:|
| 2025-12-30 | 119,100 | 121,200 | 118,700 | 119,900 | 19,746,300 | 0         | 0            |
| 2026-01-02 | 120,200 | 128,500 | 120,200 | 128,500 | 30,463,300 | 0         | 0            |
| 2026-01-05 | 134,600 | 138,600 | 133,600 | 138,100 | 42,863,400 | 0         | 0            |
| 2026-01-06 | 135,300 | 139,300 | 132,700 | 138,900 | 45,321,300 | 0         | 0            |
| 2026-01-07 | 143,500 | 144,400 | 137,600 | 141,000 | 46,317,400 | 0         | 0            |
| 2026-01-08 | 138,300 | 144,500 | 138,300 | 138,800 | 41,449,300 | 0         | 0            |
| 2026-01-09 | 136,000 | 140,700 | 135,200 | 139,000 | 29,520,600 | 0         | 0            |
| 2026-01-12 | 141,000 | 142,000 | 136,900 | 138,800 | 26,271,100 | 0         | 0            |
| 2026-01-13 | 139,800 | 140,200 | 136,900 | 137,600 | 22,384,700 | 0         | 0            |
| 2026-01-14 | 137,000 | 140,300 | 136,800 | 140,300 | 18,444,400 | 0         | 0            |
| 2026-01-15 | 139,000 | 144,000 | 138,300 | 143,900 | 24,701,100 | 0         | 0            |
| 2026-01-16 | 145,300 | 149,500 | 144,300 | 148,900 | 30,000,200 | 0         | 0            |
| 2026-01-19 | 147,200 | 150,600 | 146,600 | 149,300 | 22,762,500 | 0         | 0            |
| 2026-01-20 | 148,500 | 149,300 | 143,900 | 145,200 | 24,059,200 | 0         | 0            |
| 2026-01-21 | 141,900 | 149,800 | 141,800 | 149,500 | 31,703,600 | 0         | 0            |
| 2026-01-22 | 155,000 | 157,000 | 150,800 | 152,300 | 32,073,600 | 0         | 0            |
| 2026-01-23 | 154,700 | 156,000 | 150,100 | 152,100 | 25,407,500 | 0         | 0            |
| 2026-01-26 | 154,900 | 156,400 | 151,500 | 152,100 | 20,561,700 | 0         | 0            |
| 2026-01-27 | 150,500 | 159,500 | 149,200 | 159,500 | 29,423,700 | 0         | 0            |
| 2026-01-28 | 162,600 | 163,300 | 160,200 | 162,400 | 29,456,400 | 0         | 0            |
| 2026-01-29 | 166,200 | 166,600 | 157,100 | 160,700 | 36,087,200 | 0         | 0            |
| 2026-01-30 | 160,100 | 166,500 | 160,100 | 160,500 | 40,557,300 | 0         | 0            |
',
name='get_yf_stock_history', tool_call_id='call_******')
```

- 이후 이 응답까지 담아 최종 응답을 요청한다.  

```python
llm_with_tools.invoke(messages)
```

```bash
AIMessage(
    content='삼성전자의 주식 가격은 한 달 전과 비교했을 때 다음과 같습니다:\n\n- **한 달 전 (2025년 12월 30일)**: 종가 119,900원\n- **현재 (2026년 1월 30일)**: 종가 160,500원\n\n결론적으로, 삼성전자의 주식 가격은 한 달 전보다 올랐습니다.',
    ...
)
```