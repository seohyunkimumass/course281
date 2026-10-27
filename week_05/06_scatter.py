import numpy as np
from numpy import cos,sin,sqrt,newaxis,pi
import matplotlib.pyplot as plt

r = 5
n = 100
xlist = []
ylist = []
zlist = []

for theta in np.linspace(0,2*pi,n):
    for phi in np.linspace(0,pi,n):
        xlist.append(r*sin(phi)*cos(theta))
        ylist.append(r*sin(theta)*sin(phi))
        zlist.append(r*cos(phi))

plt.figure(figsize=(10,10))
plt.rc('font',size=12)
ax = plt.axes(projection='3d')
ax.scatter(xlist,ylist,zlist,s=1,c='m')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('3d plot')
plt.show()