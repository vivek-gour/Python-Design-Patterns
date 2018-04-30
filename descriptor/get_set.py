__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'


class myClass(object):

    def __init__(self, val=None, name='var'):
        self.val = val
        self.name = name

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        self.val = value


class anotherClass(object):
    x = myClass(10, 'var "x"')
    y = 5


m = anotherClass()
print(m.x)
m.x = 20
print(m.x)


class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")