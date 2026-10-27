import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit 

data3 = pd.read_excel('data3.xlsx')

c0,c1 = list(data3)    # get the column names
xs = data3[c0].to_numpy()
ys = data3[c1].to_numpy()

def polynomial(x,p0,p1,p2,p3,p4,p5):
    """Model function is polynomial up to x**5."""
    return (p0 + p1*x + p2*x**2 + p3*x**3 + p4*x**4
            + p5*x**5)

fit = Dfit(polynomial,xs,ys,varies=[True,True,True,True])
fit.plotfit(xlabel='x',ylabel='y')
fit.printfit()