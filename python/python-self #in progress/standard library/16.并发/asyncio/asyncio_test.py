import asyncio

import time
from collections import Coroutine


async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    dones, pendings = await asyncio.wait(tasks)
    print("----------")
    print(dones)
    print(pendings)

    for task in dones:
        print('Task ret: ', task.result())

# print(type(main()))


# 使用以前的装饰器方式声明协程
@asyncio.coroutine
def func1():
    yield from asyncio.sleep(3)
        # print(i)

# print(type(func1()))


# 使用现在的async/await方式声明协程
async def func2():
    for i in range(1, 11):
        print(i)
        await func1()


async def func3():
    for i in range(11, 21):
        print(i)
        await func1()

# loop = asyncio.get_event_loop()
# task_list = [func2(), func3()]
# loop.run_until_complete(asyncio.wait(task_list))


async def func4():
    for _ in range(3):
        await asyncio.sleep(1)
        print("func4")


async def func5():
    for _ in range(3):
        await asyncio.sleep(1)
        print("func5")


async def main1():
    tasks = [asyncio.ensure_future(func4()), asyncio.ensure_future(func5())]

    # 将完成的打印出来 as_completed 返回的是协程
    ab = asyncio.as_completed(tasks)
    print(ab)
    for task in ab:
        print(task)
        result = await task
        print(result)
        # print(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(main1())