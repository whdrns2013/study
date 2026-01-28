

## yfinance  

### 소개  

- 야후 파이낸스(Yahoo Finance)의 금융 데이터를 쉽게 가져올 수 있게 해주는 오픈소스 파이썬 라이브러리  
- 주가, 재무제표, 거래량 등 다양한 데이터를 데이터프레임 형태로 가져옴  
- 기능이 많음  

### 설치  

```bash
# pip 설치
pip install yfinance

# uv 설치
uv add yfinance
```

### Ticker  

#### 정의  

- 객체는 특정 주식 종목에 대한 모든 정보가 담긴 인스턴스   
- yfinance의 모든 데이터 접근은 Ticker 객체를 통해 이루어진다.    
- 종목 코드(Ticker Symbol)를 인자로 전달하여 객체를 생성한다.   

```python
import yfinance as yf

# 애플에 대한 티커
apple = yf.Ticker("AAPL")
```

- 주요 속성  

| 구분 | 호출 방식 (애플 기준) | 반환되는 내용 |
| --- | --- | --- |
| 기본 정보 | `apple.info` | 기업 설명, 시가총액, 업종 등 (딕셔너리) |
| 시세 데이터 | `apple.history()` | 시가, 고가, 저가, 종가, 거래량 (데이터프레임) |
| 재무 상태 | `apple.balance_sheet` | 자산, 부채, 자본 등 대차대조표 항목 |
| 수익성 | `apple.income_stmt` | 매출, 영업이익, 당기순이익 등 손익계산서 |
| 주주 환원 | `apple.dividends` | 배당금 지급 날짜와 금액 리스트 |

### 종목 코드  

종목 코드 확인 방법은 다음과 같다.  

[https://finance.yahoo.com/](https://finance.yahoo.com/)  

![alt text](/assets/images/yahoo_finance.png)

- 여기서 종목명 검색 결과에서, 종목의 이름 옆에 괄호 안에 써있는 게 종목 코드이다.  

![alt text](/assets/images/stock_code.png)


### 주요 속성  

### 주요 속성 (Attributes)  


| 속성명 | 설명 | 반환 형식 |
| :--- | :--- | :--- |
| info | 기업 개요, 시가총액, PER, ROE 등 요약 정보 조회 | Dictionary |
| dividends | 과거 배당금 지급 내역 (날짜 및 금액) | Pandas Series |
| splits | 과거 주식 분할 내역 및 비율 | Pandas Series |
| actions | 배당금과 주식 분할 이력을 합쳐서 제공 | Pandas DataFrame |
| major_holders | 주요 주주(내부자, 기관 등)의 지분 보유 비율 | Pandas DataFrame |
| institutional_holders | 상위 기관 투자자 명단 및 보유 현황 | Pandas DataFrame |
| news | 종목 관련 최근 뉴스 제목, 발행처, URL 목록 | List of Dicts |
| calendar | 실적 발표일, 배당락일 등 주요 일정 | Dictionary |


- info  

```python
import yfinance as yf

# get Ticker
samsung = yf.Ticker("005930.KS")

# info
print(samsung.info)
```

```bash
{'address1': '129 Samsung-Ro', 'address2': 'Maetan-3dong Yeongtong-gu'...}
```

<br>

- news

```python
import yfinance as yf

# get Ticker
samsung = yf.Ticker("005930.KS")

# news
print(samsung.news)
```

```bash
[{'id': ... 'title': "Samsung's Galaxy Z TriFold to cost $2,899"..}]
```



### 주요 메서드 (Methods)  


| 메서드명 | 설명 | 주요 파라미터 |
| :--- | :--- | :--- |
| history() | 과거 시세(Open, High, Low, Close, Volume) 조회 | period, interval, start, end |
| get_income_stmt() | 손익계산서 (매출, 영업이익, 순이익 등) 조회 | freq='annual'/'quarterly' |
| get_balance_sheet() | 대차대조표 (자산, 부채, 자본 등) 조회 | freq='annual'/'quarterly' |
| get_cashflow() | 현금흐름표 (영업, 투자, 재무 현금흐름) 조회 | freq='annual'/'quarterly' |
| get_earnings_dates() | 실적 발표일 일정 및 EPS 예상치/실제치 조회 | limit (데이터 개수) |
| get_recommendations() | 애널리스트들의 투자의견(Buy, Sell 등) 내역 조회 | - |
| get_shares_full() | 발행 주식 수의 시간 경과에 따른 변동 내역 조회 | start, end |

### 사용 시나리오  

```python


```


