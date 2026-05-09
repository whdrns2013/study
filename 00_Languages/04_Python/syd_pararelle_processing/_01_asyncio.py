import asyncio
import time

start = time.time()

def log(msg):
    print(f"{time.time() - start:4.1f}초 :: {msg}")

async def fetch_data(name, delay):
    log(f"{name} 요청 시작")
    await asyncio.sleep(delay)
    log(f"{name} 요청 완료")
    return f"{name} 결과"

async def main():
    results = await asyncio.gather(
        fetch_data("작업 A", 2),
        fetch_data("작업 B", 2),
        fetch_data("작업 C", 2),
    )

    log(f"최종 결과: {results}")

asyncio.run(main())