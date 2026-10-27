import numpy as np
from numpy import cos,sin,sqrt,newaxis,pi
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y

r = 10
n = 50
cparts=[]

for theta in np.linspace(0,2*pi,n):
    x = r*cos(theta)
    y = r*sin(theta)
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
