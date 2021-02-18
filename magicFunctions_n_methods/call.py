__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'
"""
    Using call we can make class as function
"""


class Test(object):
    def __call__(self, *args, **kwargs):
        print args
        print kwargs
        print '-' * 80

    def __init__(self):
        print "vivek"


t = Test()
Test()(1, 2, 3)
t(a=1, b=2, c=3)
t(4, 5, 6, d=4, e=5, f=6)
