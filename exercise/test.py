print([x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)])


def mydeco(func):
    def inner(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("#" * 10)

    return inner


def deco(func):
    def inner(*args, **kwargs):
        print("1")
        func(*args, **kwargs)

    return inner


@deco
@mydeco
def foo():
    print("hello")


foo()

from collections import namedtuple

a = namedtuple("vive", 'x y')
