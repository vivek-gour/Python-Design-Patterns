__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class EmotionalState(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def say_hello(self):
        pass

    @abstractmethod
    def say_goodbye(self):
        pass


class HappyState(EmotionalState):
    def say_goodbye(self):
        return "Bye, friend!"

    def say_hello(self):
        return "Hello, friend!"


class SadState(EmotionalState):
    def say_goodbye(self):
        return "Bye. Sniff, sniff."

    def say_hello(self):
        return "Hello. Sniff, sniff."


class Person(EmotionalState):
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def say_goodbye(self):
        return self.state.say_goodbye()

    def say_hello(self):
        return self.state.say_hello()


if __name__ == '__main__':
    person = Person(HappyState())
    print("Hello in happy state: " + person.say_hello())
    print("Goodbye in happy state: " + person.say_goodbye())

    person.set_state(SadState())
    print("Hello in sad state: " + person.say_hello())
    print("Goodbye in sad state: " + person.say_goodbye())
