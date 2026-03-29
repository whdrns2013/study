
## stream 적용시 한 글자씩이 아니라 한 문단씩 나오는 이슈  

### 이슈 내용  

![](/assets/images/stdout_buffer_01.gif)

- OpenAI API 를 통해 stream 응답을 받는 코드를 작성했다.  
- chatGPT 처럼 한 글자씩 응답이 오는 것을 기대했는데  
- 위처럼 한 문단씩 응답이 오는 게 아닌가  

### 문제 원인  

- 표준 출력(stdout)의 버퍼링(buffering)  
- 파이썬의 `print()`는 내부적으로 버퍼에 먼저 쌓고, 특정 조건이 되면 한 번에 출력한다.  
- 대표적인 버퍼링 출력 조건들은 아래와 같다.  

1. 버퍼가 어느정도 찼을 때  
2. 줄바꿈(`\n`)이 발생했을 때  
3. 프로그램이 종료될 때  
4. 버퍼를 강제로 비울 때 (flush)  

### 왜 평소에는 못봤을까?  

- 바로 `print(end="")` 조건 때문  
- 줄바꿈이 없기 때문에 stdout은 출력 조건이 "버퍼가 어느정도 찼을 때"가 되어버림  
- 하지만 평소에는 보통 end 조건을 걸지 않기 때문에 낯선 것  
- 아래 비교 코드를 실행해보자  

```python
# 줄바꿈이 있는 경우 -> 바로 출력됨
import time
gen = (x for x in range(1000))

for it in gen:
    print(it)
    time.sleep(0.02)
```


```python
# 줄바꿈이 없는 경우 -> 버퍼가 차는 것을 기다렸다가 출력됨
import time
gen = (x for x in range(1000))

for it in gen:
    print(it, end="")
    time.sleep(0.02)
```


### 해결  

- 버퍼를 즉시 비우는 `flush=True` 옵션을 적용  
- 이를 통해 print 내용을 바로 OS 로 전달해 출력되도록 함  

```python
# 예시 코드
...
print(chunk, end="")
...
```


![](/assets/images/stdout_buffer_02.gif)