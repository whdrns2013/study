
## AP  

### 개념  

- Average Precision  
- 여러 개의 정답 아이템이 있을 때, 각 정답이 등장할 때의 precision의 평균    
- 여러 개의 정답을, 얼마나 앞쪽에서 고르게 잘 배치되는지 평가하는 지표  

### 특징  

- 여러 정답을 고르게 상위에서 맞출수록 점수 증가  
- MRR과 다르게 전체적인" 순위의 품질을 평가  

### 사용하는 경우  

- 사용자당 여러 클릭 혹은 여러 구매 이력 (정답이 여러개인 경우)  
- 정보검색, 뉴스나 컨텐츠 추천 등  

### 수식    

#### 수식  

- 추천리스트에서 정답이 등장할 때의 precision를 합산하여, 개수로 나눠 평균을 냄  

$$
AP = \frac{1}{|Relevant|}\sum_{k=1}^{N}{P@k \cdot rel(k)}
$$

- $P@k$ : 추천 목록에서 k번째에서의 precision  
- $rel(k)$ : k번째 추천 아이템이 정답이면 1, 아니면 0  
- `|Relevant|` : 전체 정답 개수.  
- $N$ : 추천 목록의 길이. 

#### 예시  

- 추천 결과와 정답 예시  

```python
# 추천 결과
[ A, B, C, D, E ]

# 정답 아이템
[ B, D ]
```

- AP 계산 준비 표  

|k|item|rel(k)|P@k|비고|
|---|---|---|---|---|
|1|A|0|0/1 = 0||
|2|B|1|1/2 = 0.5|계산 포함|
|3|C|0|1/3 ≈ 0.333...||
|4|D|1|2/4 = 0.5|계산 포함|
|5|E|0|2/5 = 0.4||

- AP 계산  

$$
\frac{\frac{1}{2} + \frac{2}{4}}{2} = \frac{0.5 + 0.5}{2} = 0.5
$$

### 코드  

```python
def calc_ap(case):
    relevant_set = set(case["relevant"])
    sum_precision = 0
    hit = 0
    for i, item_yn in enumerate(case["recommend_result"]):
        if item_yn in relevant_set:
            hit += 1
            sum_precision += hit/(i + 1)
    return sum_precision/len(case["relevant"]) 
```


## MAP  

### 개념  

- Mean Average Precision  
- 모든 case 들의 AP 의 평균  

### 수식    

$$
AP = \frac{1}{|Relevant|}\sum_{k=1}^{N}{P@k \cdot rel(k)} \\
MAP = \frac{1}{n}\sum_{i=1}^{n}{AP(i)}
$$

### 코드  

```python
def calc_ap(case):
    relevant_set = set(case["relevant"])
    sum_precision = 0
    hit = 0
    for i, item_yn in enumerate(case["recommend_result"]):
        if item_yn in relevant_set:
            hit += 1
            sum_precision += hit/(i + 1)
    return sum_precision/len(case["relevant"]) 

def calc_mean_ap(cases):
    mean_ap = sum(calc_ap(case) for case in cases)/len(cases)
    return mean_ap
```