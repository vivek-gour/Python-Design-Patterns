__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

"""
A key difference between __getattr__ and __getattribute__ is that __getattr__ is only invoked if the attribute wasn't 
found the usual ways. It's good for implementing a fallback for missing attributes.

__getattribute__ is invoked before looking at the actual attributes on the object, and so can be tricky to implement 
correctly. You can end up in infinite recursions very easily.

New-style classes derive from object, old-style classes are those in Python 2.x with no explicit base class. But the 
distinction between old-style and new-style classes is not the important one when choosing 
between __getattr__ and __getattribute__
"""


# __getattr__
class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __getattr__(self, name):
        return 123456


t = Test()
print 'object variables: %r' % t.__dict__.keys()
print t.a
print t.b
print t.c
print t.d
print t.e
print t.f
print getattr(t, 'd')
print getattr(t, 'e')
print getattr(t, 'f')
print hasattr(t, 'x')


# __getattribute__
class test(object):
    def __getattribute__(self, item):
        return "This Func name not defined"


c = test()
print c.myfunc
