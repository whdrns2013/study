import asyncio
import time

start = time.time()

async def fetch_data(input_char:str):
    await asyncio.sleep(68-ord(input_char))
    print(f"{time.time()-start:4.1f}초 :: {input_char}")
    return input_char.lower()
    
async def main():
    results = await asyncio.gather(
        fetch_data("A"),
        fetch_data("B"),
        fetch_data("C")
    )
    print(f"\nresults :: {results}")

asyncio.run(main())