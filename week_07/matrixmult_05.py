import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
from scipy import linalg

A = np.array(((1,3),(2,4),(5,6)))
B = np.array(((2,1,4),(3,2,1)))

print(f'matmul(A,B) =\n{np.matmul(A,B)}')
print(f'matmul(B,A) =\n{np.matmul(B,A)}')