import numpy as np
from numpy import cos, sin, pi
import matplotlib.pyplot as plt
from scipy import linalg

th_1 = pi/4
th_2 = pi/2
th_3 = (3*pi)/2


R = np.array(((cos(th_1),-sin(th_1)),(sin(th_1),cos(th_1))))
R_T = np.transpose(R)
r = np.array((1,0))

print(np.matmul(R,R_T))

R_1 = np.array(((cos(th_1),-sin(th_1)),(sin(th_1),cos(th_1))))
r_1 = np.matmul(R_1,r)
print(r_1)

R_2 = np.array(((cos(th_2),-sin(th_2)),(sin(th_2),cos(th_2))))
r_2 = np.matmul(R_2,r)
print(r_2)

R_3 = np.array(((cos(th_3),-sin(th_3)),(sin(th_3),cos(th_3))))
r_3 = np.matmul(R_3,r)
print(r_3)