__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'


class abc():
    print("1")
    person = 'person'

    def __init__(self, p=None):
        print("2")
        self.person = p
        pass

    print("3")


obj = abc()
# print(obj.person)
# obj1 = abc("vivek")
# print(obj.person)
