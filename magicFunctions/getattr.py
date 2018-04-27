__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'


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
