__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

"""
    Sort list below list with 2nd element of inner list
"""
l = [[1, 2], [3, 3], [4, 1]]
print (l)
l.sort()
print (l)
l = [[1, 2], [4, 3], [3, 1]]

print(sorted(l, key=lambda x: x[0]))
print(sorted(l, key=lambda x: x[1]))
