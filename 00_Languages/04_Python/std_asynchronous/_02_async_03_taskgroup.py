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
    # TaskGroup : 이 TaskGroup 블록 안의 작업이 모두 끝날 때까지 나가지 않는다.
    # 관련 작업들을 안전하게 한 묶음으로 관리할 때 사용
    async with asyncio.TaskGroup() as tg:
        # 비동기 처리 대상 백그라운드 생성
        tg.create_task(run_washing_machine())
        tg.create_task(run_robot_vacuum())
    
        # 동기? 처리?
        await take_shower() # await : 이 작업이 끝날때까지 기다려라. 대신 다른 흐름은 중단시키지 마라
        await study()
        
        # 컨텍스트 관리가 되기 때문에 create_task로 실행한 작업들에 대해 기다리는 await을 써주지 않아도 됨
    
asyncio.run(main()) # 비동기 함수를 실행시키는 진입점에는 asyncio.run(함수)