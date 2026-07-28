import asyncio
import time

start = time.time()

async def fetch_data(data:str, duration:int):
    await asyncio.sleep(duration)
    print(f"{time.time()-start:4.1f}초 :: {data}")
    return data.lower()
    
async def main():
    tasks = [
        asyncio.create_task(fetch_data("A", 3)),
        asyncio.create_task(fetch_data("B", 2)),
        asyncio.create_task(fetch_data("C", 1))
    ]
    
    # done, pending = await asyncio.wait(tasks, timeout=3)
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print("\n완료된 작업 : ", [task.result() for task in done])
    print("\n안 끝난 작업 : ", [task for task in pending])

asyncio.run(main())