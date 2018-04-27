__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class Shape(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Rectangle::draw()")


class Square(Shape):
    def draw(self):
        print("Square::draw()")


class Circle(Shape):
    def draw(self):
        print("Circle::draw()")


class ShapeMaker:
    def __init__(self):
        self.circle = Circle()
        self.rectangle = Rectangle()
        self.square = Square()

    def draw_circle(self):
        self.circle.draw()

    def draw_rectangle(self):
        self.rectangle.draw()

    def draw_square(self):
        self.square.draw()


if __name__ == '__main__':
    shape_maker = ShapeMaker()

    shape_maker.draw_circle()
    shape_maker.draw_rectangle()
    shape_maker.draw_square()
