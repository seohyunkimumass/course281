import numpy as np
from numpy import cos,sin,sqrt,newaxis,arctan2
import matplotlib.pyplot as plt

xs = np.linspace(-4,4,9)
ys = np.linspace(-4,4,9)[:,np.newaxis]
print(xs)
print()
print(ys)

def w(x,y):
    r = sqrt(x**2+y**2)
    th = arctan2(y,x)
    return cos(r + th/2)
    

ws = w(xs,ys)
print(ws)
plt.imshow(ws)
plt.show()
