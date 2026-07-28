## Recall  

### 개념  

- 정답 아이템 리스트 중 추천 리스트에 포함된 아이템의 비율  
- 보통은 K 개의 추천리스트에 대한 비율을 계산하는 `Recall@K` 를 사용한다.  

### 수식  

$$
Recall@K = \frac{|R \cap K|}{|R|}
$$

- $R$ : relevant item list  
- $K$ : top-k recommended item list  

### 코드  

```python
case = {
    "recommend_result" : [7, 5, 6, 13, 2, 10, 9, 8],
    "relevant_items" : [7, 15, 5, 50]
}

def calc_recall(recommend_result, relevant_items, k:int=None):
    if k is None:
        k = len(recommend_result)
    recommend_result_k = recommend_result[:k]
    recall = len(set(recommend_result_k) & set(relevant_items)) / len(relevant_items)
    # 추천 리스트에는 중복이 없다고 가정한다.
    return recall

calc_recall(case["recommend_result"], case["relevant_items"], 5)

# >> 0.5
```

## Mean Recall  

### 개념  

- 모든 case 들의 Recall 의 평균  

### 수식  

$$
Mean \, Recall@K = \frac{1}{n}\sum_{i=1}^{n}\frac{|R_{i} \cap K_{i}|}{|R_{i}|}
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

def calc_recall(recommend_result, relevant_items, k:int=None):
    if k is None:
        k = len(recommend_result)
    recommend_result_k = recommend_result[:k]
    recall = len(set(recommend_result_k) & set(relevant_items)) / len(relevant_items)
    # 추천 리스트에는 중복이 없다고 가정한다.
    return recall

def calc_mean_recall(cases, k:int=None):
    mean_r = sum(calc_recall(case["recommend_result"], case["relevant_items"], k) for case in cases) / len(cases)
    return mean_r

calc_mean_recall(cases, 3)
# >> 0.25
```

