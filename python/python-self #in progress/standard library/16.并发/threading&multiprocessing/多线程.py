import time
from threading import Thread


def func1():
    print("func1------1")
    time.sleep(5)
    print("func1------1")


def func2():
    print("func2------1")
    time.sleep(2)
    print("func2------2")
    time.sleep(2)
    print("func2------3")


def func3():
    print("func3")
    i = 1
    while True:
        i = i ** 2
        i += 1


def func4():
    print("func4------1")
    time.sleep(2)
    print("func4------2")


def run1():
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t1.start()
    t2.start()


def run2():
    t1 = Thread(target=func3)
    t2 = Thread(target=func4)
    t1.start()
    t2.start()
    print("join")
    t1.join()
    t2.join()


def func5():
    i = 0
    while True:
        i += 1
        print(i)


def run3():
    t1 = Thread(target=func5)
    t2 = Thread(target=func5)
    t3 = Thread(target=func5)
    t1.start()
    t2.start()
    t3.start()


run3()