"""Read some data from a file and plot with error bars."""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit 

data2 = pd.read_excel('data2.xlsx')
#print(list(data2))

c0,c1,c2 = list(data2)    # get the column names
xs = data2[c0].to_numpy()
ys = data2[c1].to_numpy()
yerrs = data2[c2].to_numpy()

def polynomial(x,p0,p1,p2,p3,p4,p5):
    """Model function is polynomial up to x**5."""
    return (p0 + p1*x + p2*x**2 + p3*x**3 + p4*x**4
            + p5*x**5)

# Do three fits using 2, 3, 4 terms.
linfit = Dfit(polynomial,xs,ys,yerrs,varies=[True,True])
quadfit = Dfit(polynomial,xs,ys,yerrs,varies=[True,True,True])
cubfit = Dfit(polynomial,xs,ys,yerrs,varies=[True,True,True,True])

# Plot and print results.
linfit.plotfit(xlabel='t (s)',ylabel='y (V)')
linfit.printfit()

quadfit.plotfit(xlabel='t (s)',ylabel='y (V)')
quadfit.printfit()

cubfit.plotfit(xlabel='t (s)',ylabel='y (V)')
cubfit.printfit()