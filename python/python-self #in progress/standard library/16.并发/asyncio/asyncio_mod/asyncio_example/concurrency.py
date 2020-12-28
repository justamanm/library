import asyncio
import time
from asyncio.futures import Future
from asyncio.tasks import Task
from multiprocessing import Manager



async def say_after(delay, what):
    print(delay)
    t1 = time.time()
    await asyncio.sleep(delay)
    t2 = time.time()
    print(f"时间：{int(t2 - t1)}")
    print("await sleep1 sleep2")
    # await asyncio.sleep(delay+1)
    # t3 = time.time()
    # print(f"时间：{int(t3 - t2)}")
    # print(what)


async def main_v1():
    # 更改为两个函数
    task1 = asyncio.create_task(say_after(10, "task1"))
    task2 = asyncio.create_task(say_after(2, "task2"))

    print(f"started at {time.strftime('%X')}")
    await task1
    print("await task1 task2")
    await task2
    print(f"finished at {time.strftime('%X')}")


async def main():
    print(f"started at {time.strftime('%X')}")

    await asyncio.create_task(say_after(10, "task1"))
    print("await task1 task2")
    await asyncio.create_task(say_after(2, "task2"))

    print(f"finished at {time.strftime('%X')}")

# 异步执行
asyncio.run(main_v1())





