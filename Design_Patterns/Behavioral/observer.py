__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class WeatherSubject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_observer(self, weather_observer):
        pass

    @abstractmethod
    def remove_observer(self, weather_observer):
        pass

    @abstractmethod
    def do_notify(self):
        pass


class WeatherObserver(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_update(self, temperature):
        pass


class WeatherStation(WeatherSubject):
    def __init__(self, temperature):
        self.observers = []
        self.temperature = temperature

    def add_observer(self, weather):
        self.observers.append(weather)

    def remove_observer(self, weather):
        self.observers.remove(weather)

    def do_notify(self):
        for observer in self.observers:
            observer.do_update(self.temperature)

    def set_temperature(self, temperature):
        print("Weather station setting temperature to %s" % temperature)
        self.temperature = temperature
        self.do_notify()


class WeatherCustomer1(WeatherObserver):
    def do_update(self, temperature):
        print("Weather customer 1 just found out the temperature is: %s" % temperature)


class WeatherCustomer2(WeatherObserver):
    def do_update(self, temperature):
        print("Weather customer 2 just found out the temperature is: %s" % temperature)


if __name__ == '__main__':
    station = WeatherStation(33)

    wc1 = WeatherCustomer1()
    wc2 = WeatherCustomer2()
    station.add_observer(wc1)
    station.add_observer(wc2)

    station.set_temperature(34)
    station.remove_observer(wc1)
    station.set_temperature(35)
