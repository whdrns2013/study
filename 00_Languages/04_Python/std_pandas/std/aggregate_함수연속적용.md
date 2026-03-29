

## aggregate 함수  

### 정의  


### 문법  

```python
.aggregate()
.agg()
```



## aggregate와 groupby로 집계하기  

### 문법  

#### 각 컬럼마다 집계함수 지정하여 적용  

```python
temp_df.groupby(["OPEN_DPT_NM"]).agg({
        "ITEM1_SCORE": ["count", "mean", "std"],
        "ITEM2_SCORE": ["mean", "std"],
        "ITEM3_SCORE": ["mean", "std"],
        "ITEM4_SCORE": ["mean", "std"],
        "ITEM5_SCORE": ["mean", "std"],
        "ITEM6_SCORE": ["mean", "std"],
        "CC_TOTAL": ["mean", "std"]
})
```

- ITEM1_SCORE 만 count, mean, std를 집계하며 나머지는 모두 mean, std 집계  
- 세밀하게 조정할 수 있고, 공통 지정보다 표현 범위를 줄여 가시성  
- 다만, 하나씩 지정해야 하므로 길어짐  

#### 모든 컬럼에 공통 집계함수 지정해 적용  

```python
temp_df.groupby(["OPEN_DPT_NM"]).agg(["mean", "std", "count"])
```

- 모든 컬럼에 대해 동일한 집계함수를 지정  
- 편리하게 모든 컬럼에 지정 가능  
- 단, 세밀한 조정이 불가해 특정 컬럼에만 함수를 적용하고 싶은 경우엔 적용 불가  