## Precision

### 개념  

- 추천 리스트 중 정답 아이템이 차지하는 비율  
- 보통은 K 개의 추천리스트에 대한 비율을 계산하는 `Precision@K` 를 사용한다.  

### 수식  

$$
Precision@K = \frac{|R \cap K|}{|K|}
$$ 

- $R$ : relevant item list  
- $K$ : top-k recommended item list  

### 코드  

```python
case = {
    "recommend_result" : [7, 5, 6, 13, 2, 10, 9, 8],
    "relevant_items" : [7, 15, 5, 50]
}

def calc_precision(recommend_result, relevant_items, k:int=None):
    if k is None:
        k = len(recommend_result)
    recommend_result_k = recommend_result[:k]
    precision = len(set(recommend_result_k) & set(relevant_items)) / len(recommend_result_k)
    # 추천 리스트에는 중복이 없다고 가정한다.
    return precision

calc_precision(case["recommend_result"], case["relevant_items"], 5)

# >> 0.4
```

## Mean Precision  

### 개념  

- 모든 case 들의 Precision 의 평균  

### 수식  

$$
Mean \, Precision@K = \frac{1}{n}\sum_{i=1}^{n}\frac{|R_{i} \cap K_{i}|}{|K_{i}|}
$$

- $R$ : relevant item list  
- $K$ : top-k recommended item list  

### 코드  

```python
cases = [
    {
        'recommend_result': [7, 5, 6, 13, 2, 10, 9, 8],
        'relevant_items': [7, 15, 5, 50]
    },
    {
        'recommend_result': [30, 1, 2, 5, 22],
        'relevant_items': [3, 5]
    },
]

def calc_precision(recommend_result, relevant_items, k:int=None):
    if k is None:
        k = len(recommend_result)
    recommend_result_k = recommend_result[:k]
    precision = len(set(recommend_result_k) & set(relevant_items)) / len(recommend_result_k)
    return precision

def calc_mean_precision(cases, k:int=None):
    mean_p = sum(calc_precision(case["recommend_result"], case["relevant_items"], k) for case in cases) / len(cases)
    return mean_p

calc_mean_precision(cases, 3)
# >> 0.33333333
```
