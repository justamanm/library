import inspect


def coroutine_simple():
    print("start")
    x = yield
    print(f"received {x}")


c = coroutine_simple()
c.throw(Exception)
print(inspect.getgeneratorstate(c))
next(c)
print(inspect.getgeneratorstate(c))
try:
    c.send(1)
except:
    pass
print(inspect.getgeneratorstate(c))

