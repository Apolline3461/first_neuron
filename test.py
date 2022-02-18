import numpy as np
from util import *

# my_matrix = np.array([1, 2, 3])
# create_first_matrix(my_matrix)

# b = my_new_array()
# print(b.shape)

a1 = np.array([[1, 5], [3, 2]])
a2 = np.array([[4, 6, 8, 9], [2, 2, 2, 2], [4, 6, 8, 2], [3, 7, 1, 7]])
a3 = np.array([[7, 2], [2, 3], [1, 9], [34, 6], [23, 67]])

check_random_matrix(a1, a2, a3)

a4 = a3.dot(1)
check_mul(a4)