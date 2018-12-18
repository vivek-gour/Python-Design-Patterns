__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'

import numpy as np

"""
lst = [5, 10, 0, 200]

arr = np.array(lst)
print(arr + 5)

lst = [1, 2, 3, 'text', True, 3 + 2j]
arr = np.array(lst)

print(type(arr[0]), type(arr[4]), type(arr[5]))

print(arr.nbytes)


arr = np.array([2,5,6,8], dtype = int)
print(arr)
# [2 5 6 8]
print(type(arr))
# class 'numpy.ndarray'
print(np.result_type(arr))
# int32 
"""

''' Creation of an array with step size 1.33 between 0 - 10 '''
print(np.arange(0, 10, 1.33, dtype=np.float64))

''' Creation of an array with total 5 values between 0 - 160 '''
print(np.linspace(0, 160, 5, dtype=np.float64))

''' Method I: Using array and reshape to convert array into matrix '''
print(np.array([5, 6, 8, 45, 12, 52]).reshape(2, 3))

''' Method II: Using matrix function '''
print(np.matrix([[1, 2],
                 [3, 4]]))

''' Method III: Using misc. functions '''
print(np.eye(3))  # Identity matrix
print(np.zeros((4, 3)))
print(np.ones((3, 3), dtype=np.float64))

"""
Given two NumPy arrays arr1 = [25, 56, 12, 85, 34, 75] and arr2 = [42, 3, 86, 32, 856, 46], solve the following:

1. Create a new NumPy array Narr with the shape equal to arr1 filled with random values.

2. Permanently change the dtype of arr1 to complex.
"""
arr1 = [25, 56, 12, 85, 34, 75]
arr2 = [42, 3, 86, 32, 856, 46]
# 1.
print(np.random.rand(len(arr1)))
# 2.
print(np.array(arr1, dtype=complex))
print(np.array(arr1).astype(complex))
