__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'

"""
    When you define a magic method in your class the function will end up as a pointer in a struct that describes the 
    class, in addition to the entry in __dict__. That struct has a field for each magic method. For some reason 
    these fields are called type slots.

    Now there's another feature, implemented via the __slots__ attribute. A class with __slots__ will create 
    instances that don't have a __dict__ (they use a little bit less memory). A side-effect of this is that instances 
    cannot have other fields than what was specified in __slots__: if you try to set an unexpected field you'll get an 
    exception.
"""


class MyClass(object):
    __slots__ = ["key1", "key2", "key3"]

    def __init__(self):
        self.key1 = ""
        self.key2 = ""
        self.key3 = ""
        self.key4 = ""
