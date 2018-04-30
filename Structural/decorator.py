__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class Car(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def assemble(self):
        pass


class BasicCar(Car):
    def assemble(self):
        print("Basic Car.")


class CarDecorator(Car):
    def __init__(self, car):
        self.car = car

    def assemble(self):
        self.car.assemble()


class SportsCar(CarDecorator):
    def __init__(self, car):
        super(SportsCar, self).__init__(car)

    def assemble(self):
        super(SportsCar, self).assemble()
        print("Adding features of Sports Car.")


class LuxuryCar(CarDecorator):
    def __init__(self, car):
        super(LuxuryCar, self).__init__(car)

    def assemble(self):
        super(LuxuryCar, self).assemble()
        print("Adding features of Luxury Car.")


if __name__ == '__main__':
    sports_car = SportsCar(BasicCar())
    sports_car.assemble()
    print("-----")

    sports_luxury_car = SportsCar(LuxuryCar(BasicCar()))
    sports_luxury_car.assemble()
