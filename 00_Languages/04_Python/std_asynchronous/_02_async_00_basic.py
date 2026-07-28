import asyncio
import time

async def timer_sync():
    start = time.time()
    time.sleep(2)
    print(f"{time.time() - start:3.1f}초 :: wakeup!")

async def timer_async():
    start = time.time()
    asyncio.sleep(2)
    print(f"{time.time() - start:3.1f}초 :: wakeup!")

async def fetch_data():
    return "데이터"

async def main():
    await timer_sync()
    await timer_async()

asyncio.run(main())