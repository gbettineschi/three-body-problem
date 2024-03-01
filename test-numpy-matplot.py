import numpy as np
import matplotlib.pyplot as plt

al = np.array([[1,2,3],[2,3,4]]) # np.array contains only elements of the same type and behaves like a vector (matrix) for many reason

print(al.shape) # outputs (2,3) for 2 rows, 2 columns
print(al)
print(al[0]) # or equivalently al[0,:]
print(al[0, 1])

v = np.zeros((2,3))
print(v)

r = np.random.rand(2,3)
print(r)

# Note: in numpy each operation on arrays is done element-wise

# SCALAR MULTIPLICATION
r1 = np.random.rand(3)
r2 = np.random.rand(3)
print(np.sum(r1*r2)) # Note: numpy's sum is more efficient than Python's one