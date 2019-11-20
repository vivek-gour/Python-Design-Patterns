__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

"""
Class Method

The @classmethod decorator, is a builtin function decorator that is an expression that gets evaluated after your 
function is defined. The result of that evaluation shadows your function definition.
A class method receives the class as implicit first argument, just like an instance method receives the instance
Syntax:
"""


class C(object):
    @classmethod
    def fun(cls, arg1, arg2, *args):
        pass


# fun: function that needs to be converted into a class method
# returns: a class method for function.

"""
A class method is a method which is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter that points to the class and not the 
object instance.
It can modify a class state that would apply across all the instances of the class. For example it can modify a class 
variable that will be applicable to all the instances.
"""

"""
Static Method

A static method does not receive an implicit first argument.
Syntax:
"""


class CC(object):
    @staticmethod
    def fun(arg1, arg2, *args):
        pass


# returns: a static method for function fun
"""
A static method is also a method which is bound to the class and not the object of the class.
A static method cant access or modify class state.
It is present in a class because it makes sense for the method to be present in class.
"""

# Difference

"""
A class method takes cls as first parameter while a static method needs no specific parameters.
A class method can access or modify class state while a static method cant access or modify it.
In general, static methods know nothing about class state. They are utility type methods that take some parameters and 
work upon those parameters. On the other hand class methods must have class as parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static 
method in python.
"""

# When to use what?

"""
We generally use class method to create factory methods. Factory methods return class object 
( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
"""

from datetime import datetime


class age(object):

    def __init__(self, year, name):
        self.year = year
        self.name = name

    @classmethod
    def getAgeWithDob(cls, dob, name):
        year = datetime.strptime(dob, '%d-%m-%Y').year
        return cls(year, name)

    def printAge(self):
        age = datetime.now().year - self.year
        print("%s age is %s" % (age, self.name))


obj = age(1985, 'Vivek')
obj.printAge()
obj1 = age.getAgeWithDob('30-01-1985', 'Gour')
obj1.printAge()
