import asyncio
import time


async def say_after(delay, what):
    print(delay)
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


# started at 14:13:36
# 1
# hello
# 2
# world
# finished at 14:13:39

# main()    # 不能直接调用，coroutine 'main' was never awaited

# 顺序执行
# asyncio.run(main())


