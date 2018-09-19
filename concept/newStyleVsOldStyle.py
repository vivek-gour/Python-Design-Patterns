__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'


# if we inherit object so C will be printed and in not so A because old style work depth first
class A():
    def method(self):
        print "A"


class B(A):
    pass


class C(A):
    def method(self):
        print "C"


class D(B, C):
    pass


obj = D()
obj.method()
