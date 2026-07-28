import time
import asyncio

start = time.time()

def time_log(msg):
    print(f"{time.time()-start:4.1f}초 :: {msg}")

async def run_washing_machine():
    time_log("세탁기 시작")
    await asyncio.sleep(4)
    time_log("세탁기 종료")
    
async def run_robot_vacuum():
    time_log("로봇청소기 시작")
    await asyncio.sleep(3)
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
    await run_washing_machine()
    await run_robot_vacuum()
    await take_shower()
    await study()
    print(f"\n[최종 종료 시각] {time.time() - start:4.1f}초")

asyncio.run(main())