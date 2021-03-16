from typing import List


class MagicMethod:
    """对象描述信息"""

    b = 1
    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        # 初始化时调用
        self.a = 1

    def __str__(self):
        # 打印实例对象时调用
        pass

    def __call__(self, *args, **kwargs):
        # 将实例对象当作方法使用时，flask中就用此方法来间接调用wsgi_app方法
        pass

    def __enter__(self):
        # with语句开始执行时调用
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # with语句结束时调用，比如用来关闭文件
        pass

    def __iter__(self):
        # 有此方法的是可迭代对象；for语句所循环的是一个可迭代对象
        pass

    def __next__(self):
        # for在每次遍历获取可迭代对象的下一个元素时调用
        pass

    def __del__(self):
        # 删除对象时调用
        pass

    # def __setattr__(self, key, value):
    #     # 给属性赋值，dog.age=1是就是调用此方法
    #     # 与setattr()对应
    #     pass

    def __getattr__(self, item):
        # 获取属性值，print(dog.age)
        # 与getattr()对应
        return item

    # 类字典对象，obj[key]
    # def __getitem__(self, item):
    #     pass

    def __bool__(self):
        # if obj语句，即如何判断一个对象是true还是false，就是根据bool方法确定的
        # 内置类型都实现了自己的bool类型，自定义类就需要
        return True



# ---------------------------内置方法-----------------------
m = MagicMethod()
print(MagicMethod.__dict__)
print(m.__dict__)
# print(m.__class__)

