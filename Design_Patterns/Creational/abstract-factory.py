__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


# create an interface for Shapes
class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass


# create an interface for Colors
class Color(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def fill(self):
        pass


# create an abstract class to get factories for Color and Shape objects
class AbstractFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_color(self, color_type):
        pass

    @abstractmethod
    def get_shape(self, shape_type):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")


class Red(Color):
    def fill(self):
        print("Inside Red::fill() method.")


class Green(Color):
    def fill(self):
        print("Inside Green::fill() method.")


class Blue(Color):
    def fill(self):
        print("Inside Blue::fill() method.")


# create Factory classes extending AbstractFactory
# to generate object of concrete class based on given information.
class ShapeFactory(AbstractFactory):
    def get_shape(self, shape_type):
        if shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "RECTANGLE":
            return Rectangle()
        elif shape_type == "SQUARE":
            return Square()
        return None

    def get_color(self, color_type):
        return None


class ColorFactory(AbstractFactory):
    def get_color(self, color_type):
        if color_type == "RED":
            return Red()
        elif color_type == "GREEN":
            return Green()
        elif color_type == "BLUE":
            return Blue()
        return None

    def get_shape(self, shape_type):
        return None


# create a Factory generator/producer class
# to get factories by passing an information such as Shape or Color
class FactoryProducer:
    @staticmethod
    def get_factory(choice):
        if choice == "SHAPE":
            return ShapeFactory()
        elif choice == "COLOR":
            return ColorFactory()
        return None


if __name__ == '__main__':
    shape_factory = FactoryProducer.get_factory("SHAPE")

    shape1 = shape_factory.get_shape("CIRCLE")
    shape1.draw()

    shape2 = shape_factory.get_shape("RECTANGLE")
    shape2.draw()

    shape3 = shape_factory.get_shape("SQUARE")
    shape3.draw()

    color_factory = FactoryProducer.get_factory("COLOR")

    color1 = color_factory.get_color("RED")
    color1.fill()

    color2 = color_factory.get_color("GREEN")
    color2.fill()

    color3 = color_factory.get_color("BLUE")
    color3.fill()
