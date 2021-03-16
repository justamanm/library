
class Test:
    def test(self):
        pass


t1 = Test()


class Test:
    a = 1

    def test(self):
        pass


t2 = Test()


# TODO
# Test被重写了，但t1仍为Test对象，但没有新增的属性
# 那么，t1对象现在是存在的，但类这时还存在吗？如果类不存在，那么t1是怎么保存的？
print(type(t1), type(t2))
print(hasattr(t1, "a"))
print(hasattr(t2, "a"))
