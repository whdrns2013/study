import asyncio
import time

start = time.time()

async def boil_water(ls:list):
    await asyncio.sleep(3)
    ls.append("물 넣고 끓이기")

async def put_soup(ls:list):
    await asyncio.sleep(1)
    ls.append("라면 스프 넣기")

async def put_noodle(ls:list):
    await asyncio.sleep(2)
    ls.append("면 넣기")

async def main(ls):
    await asyncio.gather(
        asyncio.create_task(boil_water(ls)),
        asyncio.create_task(put_soup(ls)),
        asyncio.create_task(put_noodle(ls))
    )
    print(ls)

result_list = []
asyncio.run(main(result_list))

"""
참조형 자료의 경우, 따로 소유권이 있는 게 아니라 여기저기서 참조가 가능함.
따라서 구성 작업들의 소요 시간에 따라 순서가 의도치 않게 참조형 자료에 담길 수 있으니 주의
"""
