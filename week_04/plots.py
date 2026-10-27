"""arrays_slicing.py 10/01/26 SeoHyun Kim
Making some simple plots.
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos


x = np.linspace(0,25,200)

ymax = 1.0
f1 = cos(x) 
f2 = sin(x)

plt.plot(x,f1,'g--', label = 'cos(x)')
plt.plot(x,f2,'m', label = 'sin(x)')
plt.ylim(-ymax,ymax)
plt.show()
