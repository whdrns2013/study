import time
import asyncio

start = time.time()

def time_log(msg):
    print(f"{time.time()-start:4.1f}초 :: {msg}")

async def run_washing_machine(): # 비동기로 처리하고 싶은 함수 앞에는 async 키워드를 붙인다.
    time_log("세탁기 시작")
    await asyncio.sleep(4)       # await : 이 비동기 작업이 끝날 때까지 기다리되, 프로그램 전체의 다른 실행 흐름을 멈추지는 말라
    time_log("세탁기 종료")
    
async def run_robot_vacuum():
    time_log("로봇청소기 시작")
    await asyncio.sleep(3)       # time 함수는 동기이므로 블로킹이 발생한다. 블로킹을 예방하려면 asyncio.sleep 을 사용한다.
    time_log("로봇청소기 종료")

async def take_shower():
    time_log("샤워 시작")
    await asyncio.sleep(2)
    time_log("샤워 종료")

async def study():
    time_log("공부 시작")
    await asyncio.sleep(2)
    time_log("공부 종료")

async def main():
    # 비동기 처리 
    # create_task : 이 작업을 일단 백그라운드로 시작하고, 나는 다른 일을 하다가 나중에 결과를 확인하겠다.
    washing_task = asyncio.create_task(run_washing_machine())
    vacuum_task = asyncio.create_task(run_robot_vacuum())
    
    # 동기? 처리?
    await take_shower() # await : 이 작업이 끝날때까지 기다려라. 대신 다른 흐름은 중단시키지 마라
    await study()
    
    # 백그라운드 작업? 을 불러옴
    await washing_task
    await vacuum_task

asyncio.run(main()) # 비동기 함수를 실행시키는 진입점에는 asyncio.run(함수)


"""
그런데 의아한 점이 있다.  
분명 gather를 사용했을 때에는 정해진 대로 "세탁기 -> 청소기 -> 샤워" 순으로 시작됐다.  

 0.0초 :: 세탁기 시작
 0.0초 :: 로봇청소기 시작
 0.0초 :: 샤워 시작
 2.0초 :: 샤워 종료
 2.0초 :: 공부 시작
 3.0초 :: 로봇청소기 종료
 4.0초 :: 세탁기 종료
 4.0초 :: 공부 종료

하지만 create_task를 사용한 본 코드에서는 "샤워 -> 세탁기 -> 청소기 -> 공부" 순으로 시작된다.  

 0.0초 :: 샤워 시작
 0.0초 :: 세탁기 시작
 0.0초 :: 로봇청소기 시작
 2.0초 :: 샤워 종료
 2.0초 :: 공부 시작
 3.0초 :: 로봇청소기 종료
 4.0초 :: 세탁기 종료
 4.0초 :: 공부 종료

이 이유는, `create_task()`로 만들어진 작업은 "등록은 즉시"되지만, 실제 실행은 현재 main() 함수가
제어건을 양보해야 시작될 수 있기 때문이다.  
그래서 첫 번째 await을 만나기 전까지는 main() 흐름이 계속 실행되어야 하는 것이다.  
이 코드 예시로 처음 만나는 await은 await take_shower() 이므로, 해당 코드가 먼저 실행된 뒤,
등록된 task들이 순차적으로 실행되고 나서 main 함수의 흐름이 다시 진행되는 것이다.  

--> 검토 필요
"""
