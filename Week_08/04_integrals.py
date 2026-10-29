import numpy as np
from numpy import cos, sin

def integral_01(a,b):
    return ((cos(a**2))-(cos(b**2)))/2

print(integral_01(1,5))