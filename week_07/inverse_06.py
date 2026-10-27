import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
from scipy import linalg

C = np.array(((1,3,2),(2,4,1),(5,6,5)))
print(C)

C_inv = linalg.inv(C)
print(C_inv)
print(C_inv@C)

