import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt

x = np.linspace(-1,1,300)

plt.subplot(321)
plt.plot(x,sin(x))
plt.title('sin(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(322)
plt.plot(x,cos(x))
plt.title('cos(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(323)
plt.plot(x,x**1)
plt.title('x')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(324)
plt.plot(x,x**2)
plt.title('$x^2$')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(325)
plt.plot(x,x**3)
plt.title('$x^3$')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(326)
plt.plot(x,x**4)
plt.title('$x^4$')
plt.xlabel('x')
plt.ylabel('y')

plt.subplots_adjust(hspace=1.0)
plt.subplots_adjust(wspace=0.3)
plt.show()