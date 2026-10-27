import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit 


data_1 = pd.read_excel('gl1.xlsx')
print(list(data_1))

from numpy import exp

# Convert the dataframe columns to Numpy arrays.
c0,c1 = list(data_1)    # get the column names
xs = data_1[c0].to_numpy()
ys = data_1[c1].to_numpy()

def gauss(x,aa,x0,w,bb0,bb1,bb2):
    """Model function: Gaussian plus linear background"""
    return aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x

# Use Dfit to fit the data.
#guesses = [1,1,1,1,1]   # parameter guesses
guesses = [1,1,1,0,0]
fit_1 = Dfit(gauss,xs,ys,p0s=guesses)

fit_1.plotfit(xlabel=c0,ylabel=c1)
fit_1.printfit()

def loren(x,aa,x0,w,bb0,bb1,bb2):
    """Model function: Lorentzian plus linear background"""
    return aa/(1 + ((x-x0)/w)**2) + bb0 + bb1*x

guesses = [1,1,1,0,0]
fit_2 = Dfit(loren,xs,ys,p0s=guesses)

fit_2.plotfit(xlabel=c0,ylabel=c1)
fit_2.printfit()