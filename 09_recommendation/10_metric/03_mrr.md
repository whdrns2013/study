
## RR  

### 개념  

- Reciprocal Rank  
- "정답" 데이터가 "Top-K 추천 리스트" 에서 몇 번째에 등장했는지  
- 즉, 사용자가 선호하는 아이템이 얼마나 빨리 추천 리스트에 처음 등장했는지에 대한 지표이다.  

### 특징  

- "가장 먼저 등장하는 정답" 1개만을 기준으로 평가된다  
- 1등과 2등이 차이가 크다. (정답이 1등으로 등장하면 `1`, 2등이면 `0.5`)  

### 사용하는 경우  

- "가장 먼저 맞추는 것"이 중요한 서비스 (e.g. 검색, Q&A)  
- 혹은 정답이 1개인 경우  

### 수식    

$$
RR = \frac{1}{rank}
$$

### 코드  

```python
case = {
    "recommend_result" : [7, 3, 6, 13, 2],
    "relevant_items" : [6, 15, 5, 50]
    }

def calc_rr(case):
    for i, item in enumerate(case["recommend_result"]):
        if item in case["relevant_items"]:
            return 1 / (i + 1)
    return 0

print(calc_rr(case))
```

```bash
0.333333333..
```


## MRR  

### 개념  

- Mean Reciprocal Rank  
- 모든 case 들의 RR 의 평균  

### 수식    

$$
MRR = \frac{1}{n}\sum_{i=1}^{n}{\frac{1}{rank}}
$$

- $n$ : number of cases  

### 코드  

```python
cases = [
    {
        'recommend_result': [7, 5, 6, 13, 2],
        'relevant_items': [7, 15, 5, 50]
    },
    {
        'recommend_result': [30, 1, 2, 5, 22],
        'relevant_items': [3, 5]
    },
]

def calc_rr(case):
    for i, item in enumerate(case["recommend_result"]):
        if item in case["relevant_items"]:
            return 1 / (i + 1)
    return 0

def calc_mean_rr(cases) :
    mrr = sum(calc_rr(case) for case in cases) / len(cases)
    return mrr

print(calc_mean_rr(cases))
```

```bash
0.625
```