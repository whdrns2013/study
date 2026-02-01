
## 스트림 방식으로 출력하기  

### 언어 모델만 있을 때 스트림 방식으로 출력하기  

- 단순 텍스트 응답을 스트림으로 출력하는 것은 `model.stream()` 메서드를 사용하면 된다.  

```python
messages = [HumanMessage("베트맨과 볼드모트의 관계에 대해 소설 작가의 입장에서 100자 가량으로 분석해줘.")]

for c in llm.stream(messages):
    print(c.content, end="|")
```

```bash
|베|트|맨|과| 볼|드|모|트|는| 각각| 정의|와| 악|을| 상|징|하는| 캐|릭|터|로|,| 그|들의| 관계|는| 전|통|적인| 영|웅|과| 악|당|의| 대|립| 구조|를| 형|성|한다|.| 베|트|맨|은| 공|정|함|과| 정의|를| 위해| 싸|우|는| 반|면|,| 볼|드|모|트|는| 절|대| 권|력을| 추|구|하며| 혼|돈|을| 야|기|한다|.| 이|들의| 대|결|은| 인간| 내|면|의| 갈|등|과| 윤|리를| 탐|구|하며|,| 각|자의| 신|념|과| 선택|이| 중요한| 테|마|로| 작|용|한다|.||||
```

- stream 되는 전체 메시지 구조를 살펴보자  

```python
messages = [HumanMessage("베트맨과 볼드모트의 관계에 대해 소설 작가의 입장에서 100자 가량으로 분석해줘.")]
response = llm.stream(messages)

is_first = True
for chunk in response:
    print("chunk type : ", type(chunk))
    if is_first:
        is_first = False
        gathered = chunk
    else:
        gathered += chunk
    
    print("content: ", gathered.content)

messages.append(gathered)
```

```bash
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'> content:  
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'> content:  베
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'> content:  베트
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'> content:  베트맨
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'> content:  베트맨과
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'> content:  베트맨과 볼
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'> content:  베트맨과 볼드
...
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'>
content:  베트맨과 볼드모트는 각각 정의와 악의 상징으로 대립합니다. 베트맨은 고통받은 과거를 가진 영웅으로서 정의를 추구하고, 볼드모트는 권력과 불사의 욕망에 사로잡힌 악당입니다. 이들의 갈등은 인간의 선택과 도덕적 딜레마를 드러내며, 선과 악의 경계를 탐구하는 중요한 주제입니다
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'>
content:  베트맨과 볼드모트는 각각 정의와 악의 상징으로 대립합니다. 베트맨은 고통받은 과거를 가진 영웅으로서 정의를 추구하고, 볼드모트는 권력과 불사의 욕망에 사로잡힌 악당입니다. 이들의 갈등은 인간의 선택과 도덕적 딜레마를 드러내며, 선과 악의 경계를 탐구하는 중요한 주제입니다.
```

### Tool을 추가했을 때 스트림 출력하기  

- Tools 를 사용하는 시나리오에서 스트림 출력 구조를 살펴본다  

```python
messages = [HumanMessage("하와이는 몇시야?")]
response = llm_with_tools.stream(messages)

is_first = True
for chunk in response:
    print("chunk type : ", type(chunk))
    if is_first:
        is_first = False
        gathered = chunk
    else:
        gathered += chunk
    
    print("content: ", gathered.content, "tool_call_chunk: ", gathered.tool_calls)

messages.append(gathered)
```

```bash
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'>
content:   tool_call_chunk:  [{'name': 'get_current_time', 'args': {}, 'id': '...', 'type': 'tool_call'}]
...
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'>
content:   tool_call_chunk:  [{'name': 'get_current_time', 'args': {'gct_input': {}}, 'id': '...', 'type': 'tool_call'}]
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'>
content:   tool_call_chunk:  [{'name': 'get_current_time', 'args': {'gct_input': {'timezone': ''}}, 'id': '...', 'type': 'tool_call'}]
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'>
content:   tool_call_chunk:  [{'name': 'get_current_time', 'args': {'gct_input': {'timezone': 'Pacific'}}, 'id': '...', 'type': 'tool_call'}]
...
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'>
content:   tool_call_chunk:  [{'name': 'get_current_time', 'args': {'gct_input': {'timezone': 'Pacific/Honolulu', 'location': 'Hawaii'}}, 'id': '...', 'type': 'tool_call'}]
chunk type :  <class 'langchain_core.messages.ai.AIMessageChunk'>
content:   tool_call_chunk:  [{'name': 'get_current_time', 'args': {'gct_input': {'timezone': 'Pacific/Honolulu', 'location': 'Hawaii'}}, 'id': '...', 'type': 'tool_call'}]
```

- gatgered 의 tool_calls에는 계속해서 툴 콜링의 내용이 쌓이게 된다.  
- 그리고 툴 콜링 메시지가 모두 쌓이면 도구를 호출하게 하면 된다.  

```python
for tool_call in gathered.tool_calls:
    selected_tool = tool_dict[tool_call["name"]]
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)

messages
```

```bash
[
    HumanMessage(content='하와이는 몇시야?', additional_kwargs={}, response_metadata={}),
    AIMessageChunk(content='', ... tool_calls=[{'name': 'get_current_time', 'args': {'gct_input': {'timezone': 'Pacific/Honolulu', 'location': 'Hawaii'}}}], tool_call_chunks=[{'name': 'get_current_time', 'args': '{"gct_input":{"timezone":"Pacific/Honolulu","location":"Hawaii"}}',}] ...),
    ToolMessage(content='Pacific/Honolulu (Hawaii) 현재 시각 : 2026-01-31 07:21:38', name='get_current_time', ...)
]
```

- 위 메시지를 확인해보면, 최종적으로 ToolMessage에 get_current_time  함수의 실행 결과가 추가된 것을 볼 수 있다.  
- 이렇게 쌓인 메시지들을 llm에 stream 하게 만들면 된다.  

```python
for c in llm_with_tools.stream(messages):
    print(c.content, end="|")
```

```bash
|하|와|이|의| 현재| 시|각|은| |202|6|년| |1|월| |31|일|,| |07|:|21|:|38|입니다|.||||
```