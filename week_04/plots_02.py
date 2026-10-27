"""arrays_slicing.py 10/01/26 SeoHyun Kim
More Simple Plots.
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos


x = np.linspace(0,5,20)

ymax = 1.1
f1 = cos(x)
f2 = sin(x)

plt.plot(x,f1,'g--', label = 'cos(x)')
plt.plot(x,f2,'m', label = 'sin(x)')

plt.title(r'Plot of $\sigma = \cos(x)$ & $\delta = \sin(x)$', fontsize = 20)
plt.xlabel('x', fontsize = 10)
plt.ylabel('sin(x) or cos(x)', fontsize = 10)
plt.legend(fontsize=12)
plt.ylim(-ymax,ymax)
plt.show()
