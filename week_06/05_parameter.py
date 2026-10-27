import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit 

p4data = pd.read_excel('peak4.xlsx')
print(list(p4data))

from numpy import exp

# Convert the dataframe columns to Numpy arrays.
c0,c1 = list(p4data)    # get the column names
xs = p4data[c0].to_numpy()
ys = p4data[c1].to_numpy()

def gauss(x,aa,x0,w,bb0,bb1,bb2):
    """Model function: Gaussian plus linear background"""
    return aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x + bb2*x**2

# Use Dfit to fit the data.
#guesses = [1,1,1,1,1]   # parameter guesses
guesses = [3,5,1,1,0]
p4fit = Dfit(gauss,xs,ys,p0s=guesses)

p4fit.plotfit(xlabel=c0,ylabel=c1)
p4fit.printfit()