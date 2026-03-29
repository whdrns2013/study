










## HIT-RATE  

### 개념  

- (1) Top-K 추천 안에 정답 아이템 몇 개가 있는지에 대한 비율   
- (2) 정답 아이템 리스트의 아이템 중 몇 개가 Top-K 추천 리스트에 있는지에 대한 비율  
- 관례적으로 쓰이는 이름이며, 엄밀하게 표준화된 지표는 아니다.  

### 수식 및 코드  

#### (1) Top-K 추천 리스트 중 정답 아이템 개수 비율  

$$
H(R, K) = \frac{|R \cap K|}{|K|}
$$ 

- $R$ : relevant item list  
- $K$ : top-k recommended item list  

```python
# Top-5
recommend_result = [7, 5, 6, 13, 2]
relevant_items = [7, 15, 5, 50]

hit_rate = len(set(recommend_result) & set(relevant_items)) / len(recommend_result)
print(hit_rate)
```

```bash
0.4
```

#### (2) 정답 아이템 리스트 중 Top-K 추천 리스트 포함 비율  

$$
H(R, K) = \frac{|R \cap K|}{|R|}
$$ 

```python
# Top-5
recommend_result = [7, 5, 6, 13, 2]
relevant_items = [7, 15, 5, 50]

hit_rate = len(set(recommend_result) & set(relevant_items)) / len(relevant_items)
```

```bash
0.5
```

## Mean HIT-RATE  

### 개념  

- 모든 case 들의 HIT-RATE 의 평균  

### 수식 및 코드  

#### 수식  

$$
H(R, K) = \frac{|R \cap K|}{|R|} \\
mean_H(cases) = \frac{\sum_{i=1}^{n}{H(R, K)}}{n}
$$ 

- $R$ : relevant item list  
- $K$ : top-k recommended item list  
- $n$ : number of cases  

#### 코드  

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

def calc_hitrate_1(case, k:int=None) -> float:
    if k is None:
        k = len(case["recommend_result"])
    recommend_result = case["recommend_result"][:k]
    relevant_items = case["relevant_items"]
    hitrate = len(set(recommend_result) & set(relevant_items)) / len(relevant_items) # 1번 방식 hit-rate
    return hitrate

def calc_hitrate_2(case, k:int=None) -> float:
    if k is None:
        k = len(case["recommend_result"])
    recommend_result = case["recommend_result"][:k]
    relevant_items = case["relevant_items"]
    hitrate = len(set(recommend_result) & set(relevant_items)) / len(recommend_result) # 2번 방식 hit-rate
    return hitrate

def calc_mean_hitrate(cases, k:int=None) -> float:
    mean_hitrate = sum(calc_hit_rate2(case, k) for case in cases) / len(cases)
    return mean_hitrate

print(f"mean hitrate :: {calc_mean_hitrate(cases)}")
```

```bash
mean hitrate :: 0.3
```

