import requests
from typing import Literal
import time

RequestMethod = Literal["get", "post", "put", "delete", "patch", "options", "head"]

def main():
    start_time = time.time()
    sync_get()
    async_get()
    sync_post()
    async_post()
    print(f"time : {time.time() - start_time}")

def request(url:str=None, method:RequestMethod="get", headers=None, body=None):
    # make header and body
    headers = {} if headers is None else headers
    # branch by method
    requestor = getattr(requests, method) # 대박!
    response = requestor(url, headers=headers, json=body)
    return response

def sync_get():
    url = "http://localhost:18000/sync_get"
    method = "get"
    response = request(url, method)
    print(response.json())

def async_get():
    url = "http://localhost:18000/async_get"
    method = "get"
    response = request(url, method)
    print(response.json())

def sync_post():
    url = "http://localhost:18000/sync_post"
    method = "post"
    headers = {"Content-Type":"application/json"}
    body = {"param_1":10, "param_2":20}
    response = request(url, method, headers=headers, body=body)
    print(response.json())

def async_post():
    url = "http://localhost:18000/async_post"
    method = "post"
    headers = {"Content-Type":"application/json"}
    body = {"param_1":10, "param_2":20}
    response = request(url, method, headers=headers, body=body)
    print(response.json())

main()