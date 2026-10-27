import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import sqrt
from dfit import Dfit 

decay1 = pd.read_excel('decay1.xlsx')
decay2 = pd.read_excel('decay2.xlsx')

c0,c1 = list(decay1)    # get the column names
xs1 = decay1[c0].to_numpy()
ys1 = decay1[c1].to_numpy()

print(ys1)

ys1_new = ([])
for i in ys1:
    ys1_new = np.append(ys1_new,sqrt(i))
print(ys1_new)

plt.xlabel('x')
plt.ylabel('y')
plt.plot(xs1,ys1,'bo')
plt.errorbar(xs1,ys1-ys1_new,fmt='bo--',capsize=5)
plt.show()

d0,d1 = list(decay2)    # get the column names
xs2 = decay2[d0].to_numpy()
ys2 = decay2[d1].to_numpy()

plt.xlabel('x')
plt.ylabel('y')
plt.plot(xs2,ys2,'bo')
plt.show()