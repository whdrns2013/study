

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

#### 주요 속성  

| 구분 | 호출 방식 (애플 기준) | 반환되는 내용 |
| --- | --- | --- |
| 기본 정보 | `apple.info` | 기업 설명, 시가총액, 업종 등 (딕셔너리) |
| 시세 데이터 | `apple.history()` | 시가, 고가, 저가, 종가, 거래량 (데이터프레임) |
| 재무 상태 | `apple.balance_sheet` | 자산, 부채, 자본 등 대차대조표 항목 |
| 수익성 | `apple.income_stmt` | 매출, 영업이익, 당기순이익 등 손익계산서 |
| 주주 환원 | `apple.dividends` | 배당금 지급 날짜와 금액 리스트 |

### 종목 코드  

종목 코드 확인 방법에는 두 가지가 있다.  

#### (1) Yahoo! Finance 홈페이지에서 확인  

[https://finance.yahoo.com/](https://finance.yahoo.com/)  

![alt text](/assets/images/yahoo_finance.png)

- 여기서 종목명 검색 결과에서, 종목의 이름 옆에 괄호 안에 써있는 게 종목 코드이다.  

![alt text](/assets/images/stock_code.png)

#### (2) 




### 주요 속성  



### 주요 메서드  





