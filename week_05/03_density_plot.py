import numpy as np
from numpy import cos,sin,sqrt,newaxis,arctan2
import matplotlib.pyplot as plt

xs = np.linspace(-4,4,9)
ys = np.linspace(-4,4,9)[:,np.newaxis]
print(xs)
print()
print(ys)

def f(x,y):
    r = sqrt(x**2+y**2)
    th = arctan2(y,x)
    return cos(r + th)

fs = f(xs,ys)
print(fs)
plt.imshow(fs)
plt.show()
