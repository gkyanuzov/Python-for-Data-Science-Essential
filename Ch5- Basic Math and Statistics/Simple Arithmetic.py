import numpy as np
from numpy.random import randn

# only 2 nums after decimal point
np.set_printoptions(precision=2)

""""

Creating arrays

"""

# using a list
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([[10, 20, 30], [40, 50, 60]])

# via assignment
np.random.seed(25)
c = 36 * np.random.randn(6)

d = np.arange(1, 35)

print(a)
print(b)
print(c)
print(d)

""""

Performing arithmetic on arrays

"""
print("----------------")
print(a*10)
print(c + a)
print(c - a)
print(c * a)