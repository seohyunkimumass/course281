"""tryplot.py 9/29/2026 SeoHyun Kim
try out plotting.
"""

import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt

xs = np.linspace(-10,10,300)
ys = cos(xs)

plt.plot(xs,ys)
plt.show()