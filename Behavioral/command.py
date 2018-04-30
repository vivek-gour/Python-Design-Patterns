__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


class LunchCommand(Command):
    def __init__(self, lunch):
        self.lunch = lunch

    def execute(self):
        self.lunch.make_lunch()


class DinnerCommand(Command):
    def __init__(self, dinner):
        self.dinner = dinner

    def execute(self):
        self.dinner.make_dinner()


class Lunch:
    def make_lunch(self):
        print("Lunch is being made")


class Dinner:
    def make_dinner(self):
        print("Dinner is being made")


class MealInvoker:
    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()


if __name__ == '__main__':
    lunch = Lunch()  # receiver
    command_lunch = LunchCommand(lunch)  # concrete command

    dinner = Dinner()  # receiver
    command_dinner = DinnerCommand(dinner)  # concrete command

    meal_invoker = MealInvoker(command_lunch);  # invoker
    meal_invoker.invoke()

    meal_invoker.set_command(command_dinner)
    meal_invoker.invoke()
