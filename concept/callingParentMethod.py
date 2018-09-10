__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'


class MyClassA(object):

    def __init__(self, val):
        self.val = val

    def do_something(self):
        print("print from A class")


class MyClassB(MyClassA):

    def __init__(self, val):
        super(MyClassB, self).__init__(val)

    def do_something(self):
        print("print from B class")


if __name__ == "__main__":
    obj = MyClassB("vivek")
    super(MyClassB, obj).do_something()