import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
from scipy import linalg

A = np.array(((1,4,1),(4,-1,-1),(2,1,3)))
a = np.array((-4,3,7))

x,y,z = linalg.inv(A)@a
print(x,y,z)

x,y,z = linalg.solve(A,a)
print(x,y,z)

print(np.matmul(A,(x,y,z)))