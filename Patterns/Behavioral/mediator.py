__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class User(object):
    __metaclass__ = ABCMeta

    def __init__(self, med, name):
        self.mediator = med
        self.name = name

    @abstractmethod
    def send(self, msg):
        pass

    @abstractmethod
    def receive(self, msg):
        pass


class ChatMediatorImpl:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, msg, user):
        for u in self.users:
            if u != user:
                u.receive(msg)


class UserImpl(User):
    def send(self, msg):
        print(self.name + ": Sending Message: " + msg)
        self.mediator.send_message(msg, self)

    def receive(self, msg):
        print(self.name + ": Received Message: " + msg)


if __name__ == '__main__':
    mediator = ChatMediatorImpl()
    user1 = UserImpl(mediator, "John")
    user2 = UserImpl(mediator, "Lisa")
    user3 = UserImpl(mediator, "Maria")
    user4 = UserImpl(mediator, "David")
    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)
    mediator.add_user(user4)

    user1.send("Hi All")
