import numpy as np
from numpy import cos, sin, pi
import matplotlib.pyplot as plt
from scipy import linalg

rng = np.random.default_rng() # get a random number generator
# use it to make some arrays of normally-distributed numbers.
x = rng.normal(size=100)
y = rng.normal(size=100)

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'bo')
plt.show()