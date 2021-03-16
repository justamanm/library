

def sub_gen(name, num):
    print(name)
    # yield from [i for i in range(1, num)]
    for i in range(1, num):
        yield i
    return "a"


def proxy_gen():
    print("proxy")
    ret1 = yield from sub_gen("sub1", 15)
    print(ret1)
    print("-----")

    yield from sub_gen("sub2", 5)


# print(hasattr(sub_gen("test", 1), "close"))

m = proxy_gen()
print(next(m))
print(next(m))
print(m.send(None))

# 关闭所有
# m.close()
# print(next(m))  # 会抛出StopIteration

# 如果子生成器没有throw()方法，则委托生成器抛出GeneratorExit
# m.throw(ZeroDivisionError)


# print(m.send(StopIteration))

# next(m)
# print(next(m))


print("-----------------")
def test_gen(name, num):
    print(name)
    # yield from [i for i in range(1, num)]
    # for i in range(1, num):
    try:
        a = yield cfrom [1,2,3,4,5]
    # except GeneratorExit:
    #     break
    # except StopIteration:
    #     break
    except Exception as e:
        print(f"异常：{str(e)}")
        pass
    return "a"


def test_sub_gen():
    for i in range(10):
        try:
            a = yield i
        except Exception as e:
            break
    return 100


def test_proxy_gen():
    try:
        a = yield from test_sub_gen()
    except StopIteration as e:
        print(e.value)


s = test_sub_gen()
print(next(s))
# print(s.send(StopIteration))
try:
    s.throw(ZeroDivisionError)
except Exception as e:
    print(e.value)
# print(next(s))

