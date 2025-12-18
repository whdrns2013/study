
## DCG  

### 개념  

- Discounted Cumulative Gain   
- 관련도 점수와 추천에 등장한 순위에 따라 감쇠하여 누적한 랭킹 품질 점수  
- 즉, 정답이 추천 목록에 얼마나 빨리 등장했는가 + 정답과 관련성이 얼마나 높은가  

### 관련도  

- 추천된 아이템이 사용자의 의도나 정답 기준에 얼마나 잘 맞는지 수치  
- e.g. 검색 및 질의 -> 질의(Query) 와 문서(Document)의 관련성  
- e.g. 추천 -> 사용자의 선호도 (별점 1~5점과 같은), 혹은 사용자-아이템 간 관련도   

|관련도|예시|
|---|---|
|사람의 선호도|0:무관, 1:조금관련, 2:관련, 3:매우관련, 4:완벽매칭|
|이진 값|0:불일치, 1:일치|
|질의-문서 일치율|0~1 사이의 실수값|

### 특징

- 랭킹의 위치를 고려한다.  
- 정답과 추천 아이템의 관련성을 고려한다.  
- 관련성의 평가 기준이 다양하다. (0~5 정수, 0~1실수, 0 or 1 등)  

### 사용하는 경우  

- 랭킹의 위치가 중요한 경우 or 정답과 추천 아이템의 관련성이 중요한 경우  
- 또는 랭킹의 위치와 관련성이 모두 중요한 경우  
- e.g. 검색 결과 : 정답이 얼마나 빨리 등장하는지와, 질문과 정답의 관련성이 얼마나 높은지 모두 고려 필요  
- e.g. 컨텐츠 추천 : 사용자가 좋아하는 컨텐츠가 얼마나 빨리 추천되었는지와, 컨텐츠와 사용자의 선호도가 얼마나 높은지 모두 고려 필요   
- e.g. 사용자의 액션 피드백 : 상품 추천 -> 사용자의 액션에 따라 관련성 점수를 무반응(0), 클릭(1), 장바구니(2), 구매(3)로 부여  

### 수식  

$$
DCG@K = \sum_{i=1}^{k}{\frac{rel_{i}}{log_{2}(i+1)}}
$$

- $rel_{i}$ : i번째 아이템의 관련성 점수  
- $i$ : 아이템의 순서  
- $k$ : 추천 목록의 길이  

### 코드  

```python
cases = [
    {
    "recommend_result" : [ "A", "B", "C"],
    "relevance" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    },
    {
    "recommend_result" : [ "A", "B", "C"],
    "relevance" : {"A":0.9, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    },
    {
    "recommend_result" : [ "D", "A", "C", "B", "E" ],
    "relevance" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    }
]

import math

def calc_dcg(case):
    dcg = 0
    for i, item in enumerate(case["recommend_result"]):
        rel = case["relevance"][item]
        dcg += rel/(math.log2(i+1+1))
    return dcg
```

## IDCG  

### 개념  

- Ideal Discounted Cumulative Gain  
- 이상적인 DCG 값  
- 완벽한, 이상적인 추천이 수행되었을 때 얻을 수 있는 DCG 값  
- DCG 값을 정규화해, 완벽한 추천 대비 어느정도의 성능을 보이는지 평가하기 위한 정규화항  

### 수식  

$$
IDCG@K = \sum_{i=1}^{k}{\frac{rel_{i}}{log_{2}{(i+1)}}}
$$

- 기본적으로 수식은 DCG와 동일하다.  
- 다만, 계산되는 "데이터"가 다르다.  

### 예시  

```python
관련도 점수 : [3, 2, 2, 1]
이상적 추천 : [3, 2, 2, 1]
```

$$
IDCG@4 = \frac{3}{log_{2}{(2)}} + \frac{2}{log_{2}{(3)}} + \frac{2}{log_{2}{(4)}} + \frac{1}{log_{2}{(5)}} = 5.6925...
$$

### 특징  

- 항상 DCG는 0보다 크며, IDCG는 DCG보다 크다.  
- NDCG는 DCG를 IDCG로 나눈(정규화한) 값이다.  
- 따라서 NDCG는 0~1 사이의 값을 가진다.  
- 단, 관련되는 아이템이 추천 목록에 하나도 없을 경우 IDCG = 0이다.  

### 코드  

```python
import math
cases = [
    {
    "recommend_result" : [ "A", "B", "C"],
    "relevance" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    },
    {
    "recommend_result" : [ "D", "A", "C", "B", "E" ],
    "relevance" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    }
]

def calc_dcg(relevance_socres):
    dcg = 0
    for i, score in enumerate(relevance_socres):
        dcg += score/(math.log2(i+1+1))
    return dcg

def calc_idcg(case):
    valid_relevance = {k:v for k,v in case["relevance"].items() if k in case["recommend_result"]}
    sorted_relevance = sorted(valid_relevance.items(), key=lambda x:x[1], reverse=True)
    relevance_socres = [r[1] for r in sorted_relevance]
    idcg = calc_dcg(relevance_socres)
    return idcg
```




## NDCG  

### 개념  

- DCG의 값을 **이론적으로 가능한 최고 점수(IDCG)로 정규화**한 값  
- DCG의 값을 0~1 사이로 정규화하여, 추천 결과가 **최선 대비 몇%의 수준인지**를 평가할 수 있다.  
- 1에 가까울수록 이상적인 랭킹에 가깝다.  

### 





## Mean NDCG  






