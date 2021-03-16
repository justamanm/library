# -*- coding: utf-8 -*-


class Dog:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = [3, 4]
        self.num_list = [[self.a, self.b, self.c]]
        print(self.num_list[0])

    def test(self):
        self.a = 3
        self.b = 4
        # 不会改变num_list中a和b的值，因为这时的num_list[0][0]指向的是1，而不是self.a
        print(self.num_list[0])

        # 会改变num_list中c的值
        self.c.append(5)
        print(self.num_list[0])

        # 除非显示的更改num_list[0][0]的指向
        self.num_list[0][0] = 0
        print(self.num_list[0])


if __name__ == '__main__':
    d = Dog()
    d.test()