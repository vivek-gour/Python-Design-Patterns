__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'


# Using meta-classes creating singleton pattern

class SingletonType(type):
    """
        Singleton pattern ensures that only one object of a particular class is ever created.
    """
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls.instance


class Singleton(object):
    __metaclass__ = SingletonType

    def do_something(self):
        print('Singleton')


s = Singleton()
ss = Singleton()
sss = Singleton()
s.do_something()
ss.do_something()
sss.do_something()

# Object of Singleton class will be same everytime
print(s)
print(ss)
print(sss)
