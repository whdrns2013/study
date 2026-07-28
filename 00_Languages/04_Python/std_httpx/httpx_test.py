import httpx
from typing import Literal
import asyncio
import time
import atexit

RequestMethod = Literal["get", "post", "put", "delete", "patch", "options", "head"]

def main():
    start_time = time.time()
    sync_get()
    # await async_get()
    sync_post()
    # await async_post()
    print(f"time : {time.time() - start_time}")

class Requestor:
    _client: httpx.Client | None = None
    
    def __init__(self):
        if Requestor._client is None:
            Requestor._client = httpx.Client()       # 최초 1회만 실행
            atexit.register(Requestor._client.close) # 종료 시 자동으로 닫기
        
    def request(self, url:str=None, method:RequestMethod="get", headers=None, body=None):
        headers = {} if headers is None else headers
        response = Requestor._client.request(method=method, url=url, headers=headers, json=body)
        return response

rc = Requestor()

def sync_request(url:str=None, method:RequestMethod="get", headers=None, body=None):
    # make header and body
    headers = {} if headers is None else headers
    # branch by method
    with httpx.Client() as client:
        response = client.request(method=method, url=url, headers=headers, json=body)
    # response = client.request(method=method, url=url, headers=headers, json=body)
    return response

async def async_request(url:str=None, method:RequestMethod="get", headers=None, body=None):
    # make header and body
    headers = {} if headers is None else headers
    # branch by method
    async with httpx.AsyncClient() as client:
        response = await client.request(method=method, url=url, headers=headers, json=body)
    return response

def sync_get():
    url = "http://localhost:18000/sync_get"
    method = "get"
    # response = sync_request(url, method)
    rq = Requestor()
    response = rq.request(url, method)
    print(response.json())

async def async_get():
    url = "http://localhost:18000/async_get"
    method = "get"
    response = await async_request(url, method)
    print(response.json())

def sync_post():
    url = "http://localhost:18000/sync_post"
    method = "post"
    headers = {"Content-Type":"application/json"}
    body = {"param_1":10, "param_2":20}
    # response = sync_request(url, method, headers=headers, body=body)
    rq = Requestor()
    response = rq.request(url, method, headers=headers, body=body)
    print(response.json())

async def async_post():
    url = "http://localhost:18000/async_post"
    method = "post"
    headers = {"Content-Type":"application/json"}
    body = {"param_1":10, "param_2":20}
    response = await async_request(url, method, headers=headers, body=body)
    print(response.json())

main()

# 아직 효율적인 코드가 아님 (비동기 이벤트 루프 안에서 동기 코드를 실행하면서 엄청난 비효율 발생)