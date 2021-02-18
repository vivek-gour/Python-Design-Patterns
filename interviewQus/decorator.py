__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'


def decorator(func):
    def method(*args, **kwargs):
        # do something
        # print("#########################")
        return func(*args, **kwargs)  # if dont return func so it will execute below line
        # print("#########################")

    return method


@decorator
def printVivek():
    print('vivek')


printVivek()

o = printVivek()