
## DCG  

### 개념  

- Discounted Cumulative Gain   
- 관련도 점수와 추천에 등장한 순위에 따라 감쇠하여 누적한 랭킹 품질 점수  
- 즉, 정답이 추천 목록에 얼마나 빨리 등장했는가 + 정답과 관련성이 얼마나 높은가  

> Discount : 랭킹의 위치가 내려갈수록 기여도를 줄이기 때문에 Discount  
> Cumulative : 누적. 각 추천 아이템에 대해 계산한 세부항을 누적합으로 더해간다.  
> Gain : 이익. 추천된 아이템과 추천 대상과의 관련성 점수가 높을 수록 지표상 이득을 보므로 Gain  

### 구성 요소  

#### Cumulative Gain 누적 이익  

$$
CG_{p} = \sum_{i=1}^{p}rel_{i}
$$

- 결과 목록(추천 결과)에 있는 모든 관련성(relevance) 값의 합  

#### Discounted Cumulative Gain 감소된 누적 이익  

$$
DCG_{p} = \sum_{i=1}^{p}{\frac{rel_{i}}{log_{2}(i+1)}}
$$

- 누적 이익(CG)의 수치를 정교화한 것.  
- 순위가 낮아질수록(i가 커질수록) 전체 값에 기여도가 낮아진다.  

$$
Exponential \, Gain \, DCG_{p} = \sum_{i=1}^{p}{\frac{2^{rel_{i}}-1}{log_{2}(i+1)}}
$$

- 위 공식은 관련도의 차이를 비선형적으로 증폭(2의 제곱수)시켜 관련도 점수의 차이를 증폭한다.  
- 주요 웹 검색 회사나 Kaggle과 같은 데이터 과학 경쟁 플랫폼 등에서 일반적으로 사용된다.  

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
DCG@K = \sum_{i=1}^{k}{\frac{rel_{i}}{log_{2}(i+1)}}\\
또는\\
DCG@K = \sum_{i=1}^{k}{\frac{2^{rel_{i}}-1}{log_{2}(i+1)}}
$$

- $rel_{i}$ : i번째 아이템의 관련성 점수  
- $i$ : 아이템의 순서  
- $k$ : 추천 목록의 길이  

> 즉, 추천 아이템의 관련성이 높을수록 지표에 대한 기여도가 높아지며(gain)  
> 추천 아이템의 순위가 낮아질수록 지표에 대한 기여도가 낮아짐(discount)  
> 그리고 gain과 discount를 적용한 세부 계산항을 누적함(cumulative)  

### 코드  

```python
case = {
    "recommend_result" : [ "A", "B", "C"],
    "relevant_items" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    }

import math

def calc_dcg(relevance_scores, k:int=None) -> float:
    if k is None:
        k = len(relevance_scores)
    relevance_scores_k = relevance_scores[:k]
    dcg = sum(score / (math.log2(i+1+1)) for i, score in enumerate(relevance_scores_k))
    return dcg

relevance_scores = [case["relevant_items"][item] for item in case["recommend_result"]]
calc_dcg(relevance_scores)

# >> 0.7654648767857287
```

## IDCG  

### 개념  

- Ideal Discounted Cumulative Gain  
- 이상적인 DCG 값. 완벽한, 이상적인 추천이 수행되었을 때 얻을 수 있는 DCG 값  
- 즉, 사용자가 실제로 선호한 item들과의 관련성(relevance)들을 내림차순으로 정렬한 데 대한 DCG값이다.  
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

- 항상 DCG는 0보다 크거나 같으며, IDCG는 DCG보다 크거나 같다.  
- NDCG는 DCG를 IDCG로 나눈(정규화한) 값이다.  
- 따라서 NDCG는 0~1 사이의 값을 가진다.  
- 단, 정답 데이터의 관련성 점수가 모두 0이거나 평가 대상 relevance가 비어있는 경우, IDCG = 0이다.  

### 코드  

```python
import math
cases = [
    {
    "recommend_result" : [ "A", "B", "C"],
    "relevant_items" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    },
    {
    "recommend_result" : [ "D", "A", "C", "B", "E" ],
    "relevant_items" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    }
]

def calc_dcg(relevance_scores, k:int=None) -> float:
    if k is None:
        k = len(relevance_scores)
    relevance_scores_k = relevance_scores[:k]
    dcg = sum(score / (math.log2(i+1+1)) for i, score in enumerate(relevance_scores_k))
    return dcg

def calc_idcg(case, k:int=None) -> float:
    if k is None:
        k = len(case["recommend_result"])
    relevant_items = sorted(case["relevant_items"].items(), key=lambda x:x[1], reverse=True)[:k]
    if len(relevant_items) == 0:
        return 0.0
    relevance_scores = [x[1] for x in relevant_items]
    idcg = calc_dcg(relevance_scores)
    return idcg

calc_idcg(cases[0])
# >> 1.347217813316522
```


## NDCG  

### 개념  

- Normalized Discounted Cumulative Gain  
- DCG의 값을 **이론적으로 가능한 최고 점수(IDCG)로 정규화**한 값  

### 특징

- DCG의 값을 0~1 사이로 정규화하여, 추천 결과가 **최선 대비 몇%의 수준인지**를 평가할 수 있다.  
- 1에 가까울수록 이상적인 랭킹에 가깝다.  

### 수식  

$$
NDCG@K = \frac{DCG@K}{IDCG@K}
$$

### 코드  

```python
cases = [
    {
    "recommend_result" : [ "A", "B", "C"],
    "relevant_items" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    },
    {
    "recommend_result" : [ "D", "A", "C", "B", "E" ],
    "relevant_items" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    }
]

import math

def calc_dcg(relevance_scores, k:int=None) -> float:
    if k is None:
        k = len(relevance_scores)
    relevance_scores_k = relevance_scores[:k]
    dcg = sum(score / (math.log2(i+1+1)) for i, score in enumerate(relevance_scores_k))
    return dcg

def calc_ndcg(case, k:int=None) -> float:
    if k is None:
        k = len(case["recommend_result"])
    recommend_result = case["recommend_result"][:k]
    ideal_relevance_scores = [x[1] for x in sorted(case["relevant_items"].items(), key=lambda x:x[1], reverse=True)[:k]]
    recommend_result_relevance_score = [case["relevant_items"].get(item, 0.0) for item in recommend_result]
    dcg = calc_dcg(recommend_result_relevance_score)
    if len(ideal_relevance_scores) == 0:
        idcg = 0.0
    else:
        idcg = calc_dcg(ideal_relevance_scores)
    if idcg == 0.0:
        return 0.0
    else:
        return dcg/idcg

calc_ndcg(cases[0])
# >> 0.6048882832133625
```

## Mean NDCG  

### 개념  

- Mean Normalized Discounted Cumulative Gain    
- 모든 case 들의 NDCG 의 평균  

### 수식    

$$
Mean \, NDCG@K = \frac{1}{n}\sum_{i=1}^{n}{NDCG@K(i)}
$$

### 코드  

```python
cases = [
    {
    "recommend_result" : [ "A", "B", "C"],
    "relevant_items" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    },
    {
    "recommend_result" : [ "D", "A", "C", "B", "E" ],
    "relevant_items" : {"A":0.1, "B":0.5, "C":0.7, "D":0.5, "E":0.1}
    }
]

import math

def calc_dcg(relevance_scores, k:int=None) -> float:
    if k is None:
        k = len(relevance_scores)
    relevance_scores_k = relevance_scores[:k]
    dcg = sum(score / (math.log2(i+1+1)) for i, score in enumerate(relevance_scores_k))
    return dcg

def calc_ndcg(case, k:int=None) -> float:
    if k is None:
        k = len(case["recommend_result"])
    recommend_result = case["recommend_result"][:k]
    ideal_relevance_scores = [x[1] for x in sorted(case["relevant_items"].items(), key=lambda x:x[1], reverse=True)[:k]]
    recommend_result_relevance_score = [case["relevant_items"].get(item, 0.0) for item in recommend_result]
    dcg = calc_dcg(recommend_result_relevance_score)
    if len(ideal_relevance_scores) == 0:
        idcg = 0.0
    else:
        idcg = calc_dcg(ideal_relevance_scores)
    if idcg == 0.0:
        return 0.0
    else:
        return dcg/idcg

def calc_mean_ndcg(cases, k:int=None) -> float:
    mean_ndcg = sum(calc_ndcg(case, k) for case in cases) / len(cases)
    return mean_ndcg

calc_mean_ndcg(cases)
# >> 0.7356022113638424
```

## Reference  

[https://en.wikipedia.org/wiki/Discounted_cumulative_gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)  




