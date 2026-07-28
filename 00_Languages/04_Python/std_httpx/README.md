## httpx  

2025년 현재, 새로운 파이썬 프로젝트, 특히 API 클라이언트나 서버 백엔드를 구축할 때는 httpx가 사실상 표준(de-facto standard)으로 자리 잡고 있습니다.  

## requests 와 httpx 비교  

### requests (전통적인 강자)  

특징: "HTTP for Humans"라는 슬로건처럼, API가 매우 직관적이고 사용하기 쉽습니다.

장점: 오랫동안 파이썬의 HTTP 표준 라이브러리였으며, 자료가 풍부하고 매우 안정적입니다.

치명적인 단점: 동기식(Synchronous)으로만 작동합니다.

즉, requests.get(...)을 호출하면, 외부 API 서버가 응답을 줄 때까지 해당 스레드(Thread)가 완전히 멈춥니다(Blocking).

스크립트나 간단한 작업에서는 문제가 안 되지만, API 서버와 같은 동시성 처리가 중요한 애플리케이션에서는 성능 저하의 주범이 됩니다.

### httpx (현대의 표준)  

특징: requests 라이브러리의 API와 거의 동일한 사용법을 제공하면서, 동기식(Sync)과 비동기식(Async)을 모두 지원합니다.

장점:

비동기 지원 (Async/Await): async / await 키워드를 지원하여, HTTP 요청을 보내고 응답을 기다리는 동안에도 다른 작업을 처리할 수 있습니다 (Non-blocking). 이는 FastAPI, Starlette, Django 3.1+ (Async) 등 현대적인 웹 프레임워크와 완벽하게 호환됩니다.

동기 지원: requests와 동일하게 동기식 코드도 지원합니다. (httpx.get(...))

HTTP/2 지원: requests는 지원하지 않는 HTTP/2 프로토콜을 지원하여 성능을 향상시킬 수 있습니다.

Client 객체: requests.Session과 동일한 역할을 하는 httpx.Client (동기) 및 httpx.AsyncClient (비동기)를 제공하여 커넥션 풀링(Connection Pooling) 등을 효율적으로 관리합니다.


## 실행 방법  

### (1) 테스트용 API 실행  

- FastAPI 기반의 테스트용 API를 실행한다.  

```bash
uv run gunicorn dummy_api:app
```

### (2) requests 테스트  

- requests_test.py 파일을 실행시켜 테스트를 수행한다.  

```bash

```



https://gemini.google.com/app/89d75b4c047673c9?hl=ko  
https://gemini.google.com/app/0459605dc0ed7723