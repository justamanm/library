import concurrent
from concurrent.futures import ProcessPoolExecutor


numbers = [1, 2, 3]


def gcd(pair):
    print(pair)
    return pair


def run():
    # 创建进程池
    with ProcessPoolExecutor(max_workers=2) as pool:
        # submit开始执行任务
        futures = [pool.submit(gcd, pair) for pair in numbers]
        print(futures)
        # as_completed等待future完成后
        for future in concurrent.futures.as_completed(futures):
            print('进入--------')
            if future.done():
                print('执行完毕')
            # 执行结果
            print(future.result())


if __name__ == '__main__':
    run()
