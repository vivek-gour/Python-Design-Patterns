__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

"""
    Find 2nd Largest number in list
"""

list1 = [23, 12, 56, 8, 90]
list1.sort()
print(list1[-2])

"""
    Find 2nd Largest number in list without using sort
"""
list1.remove(max(list1))
print(max(list1))
