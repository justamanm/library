from collections.abc import Iterable, Iterator, Container
from typing import Iterator


# ---------------------可迭代对象&迭代器-------------------
class Iterable_class:
    def __iter__(self):
        return self


iterable_obj = Iterable_class()
print(isinstance(iterable_obj, Iterable))
print(isinstance(iterable_obj, Iterator))


class Iterator_class:
    def __iter__(self):
        return self

    def __next__(self):
        pass


iterator_obj = Iterator_class()
print(isinstance(iterator_obj, Iterable))
print(isinstance(iterator_obj, Iterator))
print("---------")


# -------------------生成器------------------
def my_generator():
    i = 1
    while True:
        yield i
        i = 2


ge1 = my_generator()
print(isinstance(ge1, Iterable))
print(isinstance(ge1, Iterator))

data1 = next(ge1)
data2 = next(ge1)
data3 = next(ge1)
print(data1, data2, data3)

for i, data in enumerate(ge1):
    if i == 3:
        break
    print(data)


# ----------------range-----------------
range_obj = range(1000)
print(isinstance(range_obj, Iterable))
print(isinstance(range_obj, Iterator))


# ---------------生成器的send用法 插手迭代过程---------------
def test():
    i = 1
    while i < 5:
        yield i**2      # 不将yield语句赋值，send()不会起作用
        i = yield i**2  # 将yield语句赋值，send()发送的值会赋值给i
        i += 1


t = test()
# 第一次运行只能使用next或者send(None)
print(next(t))
print(next(t))
# send的作用相当于使生成器继续运行，并且传递的参数为yield的返回值(程序中即temp的值)
t.send(3)
print(next(t))     # 相当于send(None) 此时temp = None


# ---------------yield from用法 生成器嵌套（用于处理直接调用生成器可能出现的异常情况）---------------
print("yield from")
def sub_gen():
    i = 0
    while i < 5:
        i = yield i**2
        if i == -1:
            # return/break，意味着当前协程结束
            return "over"


def proxy_gen():
    while True:
        # 1.yield from会创建一个子生成器，之后主调用方的send()直接和子生成器交流，直到子生成器结束
        # 2.只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        ret = yield from sub_gen()
        print(ret)

        # 走到这里，由于代理生成器还在循环(while True)，所以会接着执行，再创建一个新的sub_gen生成器
        # return


def main_invoke():
    gen = proxy_gen()
    next(gen)       # 初始化生成器
    print(gen.send(1))
    print(gen.send(2))
    print(gen.send(-1))


main_invoke()