
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

async def do_my_work(): # 동기로 처리할 두 개의 작업은 하나의 흐름으로 묶음
    await take_shower()
    await study()

async def main():
    await asyncio.gather( # gather : 비동기 처리로 같이 시작할 작업 묶음 --> 이 작업들을 동시에 시작하고, 전부 끝날 때까지 기다려라
        run_washing_machine(),
        run_robot_vacuum(),
        do_my_work()
    )
    print(f"\n[최종 종료 시각] {time.time() - start:4.1f}초")

asyncio.run(main()) # 비동기 함수를 실행시키는 진입점에는 asyncio.run(함수)


