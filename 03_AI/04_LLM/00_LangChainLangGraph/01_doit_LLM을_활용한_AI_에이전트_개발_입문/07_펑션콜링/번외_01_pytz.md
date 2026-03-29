

## pytz  

### 소개  

- 파이썬에서 정확한 시간대(Timezone) 처리를 위해 사용하는 라이브러리  
- IANA Time Zone Database(Olson DB)를 기반으로 한 표준 시간대 라이브러리  
- 특히 서머타임(DST)과 과거·미래 시간대 변경 이력까지 정확히 처리해야 할 때 필요  
- datetime 기본 모듈이 갖지 못한 정확한 지역별 시간대 계산을 보완  
- 타임존 문자열을 받아 그에 해당하는 타임존 인스턴스를 생성한다.  
- 예: Asia/Seoul, Europe/Paris, US/Eastern 등 실제 지역 기반 시간대 사용 가능  


### 기본 사용 방법  

#### 기본적인 사용법  

```python
import pytz
from datetime import datetime

# 타임존 인스턴스 생성
tz_seoul = pytz.timezone("Asia/Seoul") # timezone 인스턴스 생성
tz_us_east = pytz.timezone("US/Eastern") # timezone 인스턴스 생성

# 현재 시간 비교
print(datetime.now(tz_seoul))
print(datetime.now(tz_us_east))
```

```bash
2026-01-26 22:11:53.749843+09:00
2026-01-26 08:11:53.749989-05:00
```

#### 시간대 변환    

```python
import pytz
from datetime import datetime

tz = pytz.timezone("Asia/Seoul")

dt = datetime(2026, 1, 1, 12, 0)
aware_dt = tz.localize(dt)
print(aware_dt)

# 지정한 타임존으로 변환
utc = pytz.utc
dt_utc = aware_dt.astimezone(utc)
(print(dt_utc))
```

```bash
2026-01-01 12:00:00+09:00
2026-01-01 03:00:00+00:00
```


#### 전체 시간대 목록 출력  

```python
import pytz

pytz.all_timezones
```

```bash
['Africa/Abidjan',
 'Africa/Accra',
 'Africa/Addis_Ababa',
 'Africa/Algiers',
 'Africa/Asmara',
 'Africa/Asmera',
 ...
 'W-SU',
 'WET',
 'Zulu']'
```

## Reference  

[https://pypi.org/project/pytz/](https://pypi.org/project/pytz/)  