import asyncio
import time

start = time.time()

async def fetch_data(input_char:str):
    await asyncio.sleep(68-ord(input_char))
    print(f"{time.time()-start:4.1f}초 :: {input_char}")
    return input_char.lower()
    
async def main():
    
    async with asyncio.TaskGroup() as tg:
        task_a = tg.create_task(fetch_data("A"))
        task_b = tg.create_task(fetch_data("B"))
        
        c_result = await fetch_data("C")
    
    print("out of tg block")
    print(task_a.result(), task_b.result(), c_result)

asyncio.run(main())