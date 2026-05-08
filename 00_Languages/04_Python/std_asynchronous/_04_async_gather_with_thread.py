import time
import asyncio

start = time.time()

def time_log(msg):
    print(f"{time.time()-start:4.1f}초 :: {msg}")

async def run_washing_machine(): # 비동기로 처리하고 싶은 함수 앞에는 async 키워드를 붙인다.
    time_log("세탁기 시작")
    await asyncio.sleep(4)             # await : 이 비동기 작업이 끝날 때까지 기다리되, 프로그램 전체의 다른 실행 흐름을 멈추지는 말라
    time_log("세탁기 종료")
    
async def run_robot_vacuum():
    time_log("로봇청소기 시작")
    await asyncio.sleep(3)             # time 함수는 동기이므로 블로킹이 발생한다. 블로킹을 예방하려면 asyncio.sleep 을 사용한다.
    time_log("로봇청소기 종료")

def take_shower():     # 샤워와 공부는 내가 직접 처리해야하는 동기 함수
    time_log("샤워 시작")
    time.sleep(2)
    time_log("샤워 종료")

def study():            # 샤워와 공부는 내가 직접 처리해야하는 동기 함수
    time_log("공부 시작")
    time.sleep(2)
    time_log("공부 종료")

async def do_my_work(): # 샤워와 공부를 묶어 하나의 비동기 함수로 만듦 (이 my-work는 세탁, 로봇청소기와는 비동기 처리)
    await asyncio.to_thread(take_shower) # to_thread 는 "동기 함수를 별도 스레드에서 실행해서, 이벤트 루프를 막지 않게 해주는 도구"이다.
    await asyncio.to_thread(study)

async def main():
    await asyncio.gather(
        run_washing_machine(),
        run_robot_vacuum(),
        do_my_work()
    )

asyncio.run(main())