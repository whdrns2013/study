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
    
    for task in asyncio.as_completed(tasks):
        result = await task
        print(f"처리 완료 : {result}\n")
    
asyncio.run(main())