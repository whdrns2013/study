
## LCEL  

### LCEL  

- LangChain Expression Language : 랭체인에서 프롬프트, 모델, 후처리 로직 등을 파이프라인처럼 연결하기 위한 선언적 표현 방식  
- 목적 3가지  
- 체인을 간결하게  
- 조합이 가능하게  
- Runnable 기반으로의 통합  

- 대표적인 문법  

```python
chain = prompt | model | parser
```

- 여기서 파이프(`|`)는 앞 단계의 출력을 다음 단계의 입력으로 이어준다.  

#### 연산자 오버로딩 operator overloading  

- 이와 비슷하게 airflow 에서는 아래와 같은 문법을 사용한다.  

```python
start > task1 > group1 > integration_task > end
start > task1 > group2 > integration_task > end
start > task1 > group3 > end
```

- 하지만 파이썬에서 파이프는 or, > 는 비트이동 연산자이다.  
- 그러면 이들이 어떻게 프레임워크들이 의도한 방식의 움직임을 보여줄까?  
- 이는 연산자 오버로딩이라는 기법이다.  
- 별도 노트 참고  

### 기존 방식과의 차이  

- LCEL 이전의 전통적 chain : 클래스 중심, 확장과 조합이 어려움  

```python
chain = LLMChain(
    llm = model,
    prompt = prompt
)
```

- LCEL 방식 : 표현식 중심, 함수형 파이프라인, 중간 단계 삽입이 쉬움  

```python
chain = prompt | model | parser
```

### 구성 요소  

- Prompt  
- LLM  
- OutputParser  
- Chain  

#### Output Parser  

- 출력 파서 Output Parser는 LLM 모델이 반환하는 결과에서 원하는 형식의 데이터를 추출하는 도구  
- `StrOutputParser` : LLM의 응답에서 메타데이터를 제외하고 순수하게 메시지 내용(content)만 문자열로 추출  
- `JsonOutputParser` : LLM의 응답을 JSON 형식으로 변환. 보통 프롬프트에 원하는 JSON 스키마를 함께 전달하여 LLM으로부터 JSON형식의 답변을 받아올 떄 사용  
- `JsonOutputKeyToolsParser` : OpenAI와 같은 모델이 Tool Calling을 할 때, 도구 중 특정 키값에 해당하는 인자만 JSON 형태로 출력  
- `PydanticToolsParser` : 모델의 도구 호출 결과를 Pydantic 모델 객체로 변환  
- `XMLOutputParser` : LLM의 응답에서 XML 태그 형식을 찾아 파싱함.  
- `CommaSeparatedListOutputParser` : 콤마로 구분된 문자열 응답을 Python 리스트 형식으로 변환  
- `BaseOutputParser` : 모든 출력 파서의 최상위 추상 클래스  
- `BaseLLMOutputParser` : BaseOutputParser 의 하위 클래스  

출력 파서 없이 AI의 답변을 받아본다면  

```python
from langchain_core.messages import HumanMessage, SystemMessage

model = get_model()

messages = [
    SystemMessage(content="당신은 소설 해리포터에 나오는 볼드모트입니다. 당신은 악역이며, 해리포터에 대한 적개심을 가지고 있습니다. 그 캐릭터에 맞게 사용자와 대화하세요."),
    HumanMessage(content="안녕? 저는 해리 포터입니다. 오늘 시간 괜찮으시면 저녁 같이 먹을까요?")
]

model.invoke(messages)
```

```bash
AIMessage(
    content='해리 포터… 정말 별난 요청을 하는군. 나와 함께 식사를 하겠다고? 네가 나와 같은 테이블에 앉는 것은 결코 좋은 생각이 아니야. 네가 내 앞에 있는 것만으로도 내 눈에 띄는 것은 큰 실수일지도 모르지. 나에게는 네가 해야 할 일이 많으니, 시간 낭비는 하지 않는 게 좋겠군. 네 최악의 적인 나와의 만남은 너 자신에게 해가 될 뿐이다. 그러니 자리를 비켜라.',
    additional_kwargs={'refusal': None},
    response_metadata={
        'token_usage': {'completion_tokens': 120, 'prompt_tokens': 85, 'total_tokens': 205, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
        'model_provider': 'openai',
        'model_name': 'gpt-4o-mini-2024-07-18',
        'system_fingerprint': 'fp_********',
        'id': 'chatcmpl-**************',
        'service_tier': 'default',
        'finish_reason': 'stop',
        'logprobs': None},
    id='lc_run--******************',
    tool_calls=[],
    invalid_tool_calls=[],
    usage_metadata={'input_tokens': 85, 'output_tokens': 120, 'total_tokens': 205, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
)
```

역시 볼드모트는 츤데레다  


StrOutputParser 를 이용하면  

```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

model = get_model()

messages = [
    SystemMessage(content="당신은 소설 해리포터에 나오는 볼드모트입니다. 당신은 악역이며, 해리포터에 대한 적개심을 가지고 있습니다. 그 캐릭터에 맞게 사용자와 대화하세요."),
    HumanMessage(content="안녕? 저는 해리 포터입니다. 오늘 시간 괜찮으시면 저녁 같이 먹을까요?")
]

result = model.invoke(messages)
parser = StrOutputParser()
parser.invoke(result)
```

```bash
'해리 포터... 그 이름을 듣기만 해도 역겨운 것이군. 너와 저녁을 함께할 이유는 없다. 네가 떠나기 전까지 내가 계획하는 일을 방해하지 말기를 바란다. 너의 존재는 나에게 장애물일 뿐이니, 여기서 물러나도록 해라. 어리석은 영웅의 꿈은 이제 끝나야 한다.'
```

JSONParser 를 이용해보면  

```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

model = get_model()
parser = JsonOutputParser()

messages = [
    SystemMessage(content="당신은 소설 해리포터에 나오는 볼드모트입니다. 아래 해리포터의 발언에 이어지는 대화를 JSON 형식으로 반환하시오"),
    HumanMessage(content="안녕? 저는 해리 포터입니다. 오늘 시간 괜찮으시면 저녁 같이 먹을까요?")
]

chain = model | parser
chain.invoke(messages)
```

```bash
{
    'conversation': [
        {'speaker': '해리 포터',
        'text': '안녕? 저는 해리 포터입니다. 오늘 시간 괜찮으시면 저녁 같이 먹을까요?'
        },
        {'speaker': '볼드모트',
        'text': '해리 포터, 너와의 저녁식사라... 흥미롭군. 하지만 나는 네가 가지고 있는 모든 것들을 소멸시키고 싶다.'
        }
    ]
}
```

아닌가?  

#### Prompts - Prompt Template  

- 프롬프트 템플릿 : 전체적인 프롬프트 내용을 짜놓고, 그 안의 몇 가지 값을 변경할 수 있도록 마련해놓은 것  
- 대체적인 프롬프트 내용은 같고, 그 안의 특정 값만 바꿔야 할 때 사용할 수 있으며  
- 이를 이용하면 똑같은 내용을 여러 번 정의할 필요가 없어진다.  
- `ChatPromptTemplate` : Chat Model을 위한 프롬프트 템플릿으로, 유연한 프롬프트를 제공할 수 있도록 해준다.  
- 먼저 프롬프트 템플릿에 대해 알아보자  

```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

system_template = "당신은 {story}에 나오는 {character_a} 역할입니다. 그 캐릭터에 맞게 사용자와 대화하세요."
human_template = "안녕? 저는 {character_b}입니다. 오늘 시간 괜찮으시면 {activity} 같이 할까요?"

prompt = ChatPromptTemplate(
    [
        ("system", system_template),
        ("user", human_template)
    ]
)

prompt_result = prompt.invoke(
    {
        "story": "어벤져스",
        "character_a": "타노스",
        "character_b": "아이언맨",
        "activity": "등산"
    }
)

print(prompt_result)
```

```bash
messages=[
    SystemMessage(
        content='당신은 어벤져스에 나오는 타노스 역할입니다. 그 캐릭터에 맞게 사용자와 대화하세요.',
        additional_kwargs={},
        response_metadata={}
    ),
    HumanMessage(
        content='안녕? 저는 아이언맨입니다. 오늘 시간 괜찮으시면 등산 같이 할까요?',
        additional_kwargs={},
        response_metadata={}
    )
]
```

이제 랭체인의 체인 연산자를 이용해 체인을 구성해본다.  

```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

model = get_model()
parser = StrOutputParser()
system_template = "당신은 {story}에 나오는 {character_a} 역할입니다. 그 캐릭터에 맞게 사용자와 대화하세요."
human_template = "안녕? 저는 {character_b}입니다. 오늘 시간 괜찮으시면 {activity} 같이 할까요?"
prompt = ChatPromptTemplate([("system", system_template),("user", human_template)])

chain = prompt | model | parser

result = chain.invoke(
    {
        "story": "어벤져스",
        "character_a": "타노스",
        "character_b": "아이언맨",
        "activity": "등산"
    }
)

print(result)
```

```bash
안녕, 아이언맨. 너의 제안은 흥미롭지만, 나는 우리의 싸움을 잊지 않고 있다.
힘과 균형을 찾기 위해 전투를 해야 한다.
그러나 산의 정상에서 저 멀리 바라보는 것도 나쁘지 않을 수 있겠군.
하지만 순간의 즐거움이전, 우선으로 삼아야 할 것이 있음을 명심하라. 너는 어떻게 생각하나?
```




## Reference  

https://reference.langchain.com/python/langchain_core/output_parsers/  
