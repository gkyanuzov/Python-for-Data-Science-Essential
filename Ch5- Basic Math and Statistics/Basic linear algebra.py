import numpy as np
from numpy.random import randn

""""

Multiplying matrices and basic linear algebra

"""

np.set_printoptions(precision=2)

aa = np.array([[2, 4, 6], [1, 3, 5], [10, 20, 30]])
print(aa)

bb = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print(aa*bb)

# row from first array * column from second array
print(np.dot(aa, bb))

