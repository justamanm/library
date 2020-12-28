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
        print(self.num_list[0])

        self.c.append(5)
        print(self.num_list[0])


if __name__ == '__main__':
    d = Dog()
    d.test()