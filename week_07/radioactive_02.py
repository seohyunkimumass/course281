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

def model(N_0,ta,B):
    N_0*np.exp(-t/ta) + B

N_0 = 10
ta = 50
B = 25
print(ys1)

ys1_error = ([])
for i in ys1:
    ys1_error = np.append(ys1_error,sqrt(i))
print(ys1_error)

plt.yscale('log')
plt.xlabel('x')
plt.ylabel('y')
plt.errorbar(xs1,ys1,ys1_error,fmt='bo',capsize=5)
plt.show()

d0,d1 = list(decay2)    # get the column names
xs2 = decay2[d0].to_numpy()
ys2 = decay2[d1].to_numpy()
ys2_error = ([])
for i in ys2:
    ys2_error = np.append(ys2_error,sqrt(i))
print(ys2_error)


plt.yscale('log')
plt.xlabel('x')
plt.ylabel('y')
plt.errorbar(xs1,ys1,ys2_error,fmt='bo',capsize=5)
plt.show()

# The error bars should be bigger near the ends of the plots, where the Nj values are smaller (why?).


# Both plots should look like straight lines, except possibly near the end where the background term is appreciable (why?).

