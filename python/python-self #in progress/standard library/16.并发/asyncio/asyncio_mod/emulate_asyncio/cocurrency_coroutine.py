import time
from select import select
from multiprocessing import Process


ready = []

class Future:
    state = "pending"
    def __init__(self, coro):
        self.coro = coro

    def __call__(self, *args, **kwargs):
        result = self.coro(*args, **kwargs)
        self.state = "finish"
        return result

def execute(task, *args):
    result = task(*args)
    return result


def loop_task():
    while True:
        for task_info in ready:
            result = execute(task_info[0], task_info[1][1])
            callback = task_info[2]
            callback(task_info[1][0]:corotine, result)
        time.sleep(0.1)


# 调用时，注册异步任务后直接返回
def schedule(task, *context, callback=None):
    ready.append((task, context, callback))
    return


def wake_up(coro, result):
    coro.send(result)


# 异步任务，实现中需要将异步操作，回调函数加入到loop.ready中
def sleep(*args):
    # 1.将异步任务交给一个调度器
    # 2.绑定回调函数
    task = Future(time.sleep)
    schedule(task, *args, callback=wake_up)
    return task


# TODO wrap成一个类
def corotine(self):
    print(f"{self} is executed")

    for i in range(1000):
        # 对应task_new()
        # i == 10:
        #   return "over"
        try:
            # yield i		# 在正常的逻辑中，yield只会用在堵塞操作上
            print(i)        # 非阻塞业务逻辑
            wake = yield sleep(self, 5)         # 执行异步操作，用回调函数解阻塞接着完成子任务
            print(i+1)      # 非阻塞业务逻辑
        except Exception as e:
            break
    return "over"


def task(name):
    print(f"{name} is executed")
    s = corotine()
    i = 1

    # run方法等价于
    # yield from corotine()
    while True:
        ret = s.send(None)    # 恢复执行
        if isinstance(ret, Future):
            yield           # 在这里阻塞，是为了实现并行，把执行权交给其他任务
        if i == 10:
            try:
                s.throw(ZeroDivisionError)  # 结束执行
            except Exception as e:
                print(e.value)
                break
        i += 1


def client():
    task("task1")
    task("task2")


def task_new():
    print("start")
    s1 = corotine("task1")
    s2 = corotine("task2")

    # 实际的业务逻辑中，下面的循环会仅相当于一个包含有堵塞操作的业务
    # (while True + 异常处理)的逻辑等价于yield from corotine()
    # 所以，总体等价于
    await s1
    await s2

    # i = 1
    # while True:
    #     ret = s.send(None)  # 恢复执行
    #     if isinstance(ret, Future):
    #         yield  # 在这里阻塞，是为了实现并行，把执行权交给其他任务
    #     if i == 10:
    #         try:
    #             s.throw(ZeroDivisionError)  # 结束执行
    #         except Exception as e:
    #             print(e.value)
    #             break
    #     i += 1




if __name__ == '__main__':
    p1 = Process(target=loop_task)
    p2 = Process(target=task_new)
    p1.start()
    p2.start()
