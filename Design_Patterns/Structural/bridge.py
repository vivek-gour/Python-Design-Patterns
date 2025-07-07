__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class Color(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def fill_color(self):
        pass


class Shape(object):
    __metaclass__ = ABCMeta

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def color_it(self):
        pass


class Rectangle(Shape):
    def __init__(self, color):
        super(Rectangle, self).__init__(color)

    def color_it(self):
        print("Rectangle filled with ")
        self.color.fill_color()


class Circle(Shape):
    def __init__(self, color):
        super(Circle, self).__init__(color)

    def color_it(self):
        print("Circle filled with ")
        self.color.fill_color()


class RedColor(Color):
    def fill_color(self):
        print("red color")


class BlueColor(Color):
    def fill_color(self):
        print("blue color")


if __name__ == '__main__':
    s1 = Rectangle(RedColor())
    s1.color_it()

    s2 = Circle(BlueColor())
    s2.color_it()
