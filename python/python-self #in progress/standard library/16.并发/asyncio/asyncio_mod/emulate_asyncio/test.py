from asyncio import Future

# from emulate_asyncio.runner import run
import asyncio


def do_async():
    yield from asyncio.sleep(5)


def main():
    yield from do_async()


# run(main())
class Dog():
    pass


from collections.abc import Iterable, Iterator, Generator
print(issubclass(Dog, Iterable))
print(issubclass(Dog, Iterator))
print(issubclass(Dog, Generator))


# ---------------- bug ---------------
class Dog:
    @classmethod
    def run(cls):
        for i in range(2):
            yield i


a = Dog.run
b = Dog.run

print(a == b)
print(a is b)
print(id(a), id(b))

c = Dog().run
d = Dog().run
print(c == d)
print(c is d)
print(id(c), id(d))

e = Dog.run()
for i in e:
    print(i)

next(e)

