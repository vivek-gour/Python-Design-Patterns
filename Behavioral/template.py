__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class Meal(object):
    __metaclass__ = ABCMeta

    # template method
    def do_meal(self):
        self.prepare_ingredients()
        self.cook()
        self.eat()
        self.clean_up()

    def eat(self):
        print("Mmm, that's good")

    @abstractmethod
    def prepare_ingredients(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def clean_up(self):
        pass


class HamburgerMeal(Meal):
    def prepare_ingredients(self):
        print("Getting burgers, buns, and french fries")

    def cook(self):
        print("Cooking burgers on grill and fries in oven")

    def clean_up(self):
        print("Throwing away paper plates")


class TacoMeal(Meal):
    def prepare_ingredients(self):
        print("Getting ground beef and shells")

    def cook(self):
        print("Cooking ground beef in pan")

    def eat(self):
        print("The tacos are tasty")

    def clean_up(self):
        print("Doing the dishes")


if __name__ == '__main__':
    meal1 = HamburgerMeal()
    meal1.do_meal()
    print("-----")

    meal2 = TacoMeal()
    meal2.do_meal()
    print("-----")
