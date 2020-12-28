import time


def test_gen():
    for i in range(1000):
        try:
            a = yield i		# 中断执行
            time.sleep(1)   # 这里会使得当前任务堵塞，但顺序执行会一直等到解阻塞，才会执行后续任务
        except Exception as e:
            break
    return "over"


def task(name):
    print(f"{name} is executed")
    s = test_gen()
    i = 1
    while True:
        print(s.send(None))    # 恢复执行
        if i == 10:
            try:
                s.throw(ZeroDivisionError)  # 结束执行
            except Exception as e:
                print(e.value)
                break
        i += 1


task("task1")
task("task2")