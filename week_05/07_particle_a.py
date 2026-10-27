import numpy as np
from numpy import cos,sin,sqrt,newaxis,pi
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y

cparts = []
for x in np.linspace(-5,5,40):
    for y in np.linspace(-5,5,40):
        if np.sqrt(x**2 + y**2) > 3 and np.sqrt(x**2 + y**2) < 5:
            cparts.append(Particle(x,y))
# Plot the particle positions.
for p in cparts:
    plt.plot(p.x,p.y,'mo')
plt.xlabel('x')
plt.ylabel('y')
# The plot looks better with the x and y axis scaled equally.
ax = plt.gca()       # get current axes
ax.axis('equal')
plt.show()