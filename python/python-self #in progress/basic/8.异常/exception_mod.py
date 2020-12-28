

class A(Exception):
    pass


class B(A):
    b = 2
    pass


class C(A):
    pass


try:
    raise ZeroDivisionError()
except ZeroDivisionError as e:
    raise ValueError from ZeroDivisionError("aaa")
# except B:
#
# except C:
#     print("c")

