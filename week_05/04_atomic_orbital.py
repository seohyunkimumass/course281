import numpy as np
from numpy import cos,sin,sqrt,newaxis,arctan2
import matplotlib.pyplot as plt

xs = np.linspace(-20,20,100)
ys = np.linspace(-20,20,100)[:,np.newaxis]
a_0 = 5.29*10**-11

def psi(x,y):
    r = sqrt(x**2+y**2)
    return x*(6-r)*np.e**(-r/3)

psis = psi(xs,ys)
ax = plt.axes(projection='3d')
ax.plot_surface(xs,ys,psis,cmap='plasma')
ax.set_zlim(-4,4)

plt.title('Wave Function of H ($n = 3, l = 1, m = 0)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
    
    