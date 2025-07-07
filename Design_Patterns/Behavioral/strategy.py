__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class Strategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def check_temperature(self, temperature):
        pass


class HikeStrategy(Strategy):
    def check_temperature(self, temperature):
        if 50 <= temperature <= 90:
            return True
        else:
            return False


class SkiStrategy(Strategy):
    def check_temperature(self, temperature):
        if temperature <= 32:
            return True
        else:
            return False


class Context:
    def __init__(self, temperature, strategy):
        self.temperature = temperature
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_temperature(self):
        return self.temperature

    def get_result(self):
        return self.strategy.check_temperature(temperature)


if __name__ == '__main__':
    temperature = 60

    strategy_ski = SkiStrategy()
    context = Context(temperature, strategy_ski)

    print("Is the temperature ({} F) good for skiing? {}".format(context.get_temperature(), context.get_result()))

    strategy_hike = HikeStrategy()
    context.set_strategy(strategy_hike)

    print("Is the temperature ({} F) good for hiking? {}".format(context.get_temperature(), context.get_result()))
