import numpy as np
from numpy import arctan,sqrt,newaxis,pi
import matplotlib.pyplot as plt

class RightTriangle:
    def __init__(self,y,x):
        self.x = x
        self.y = y

    def hyp(self):
        print(sqrt(self.x**2+self.y**2))

    def angle1(self):
        print(((arctan(self.x/self.y)))*(180/pi))

    def angle2(self):
        print (((arctan(self.y/self.x)))*(180/pi))

t = RightTriangle(1,sqrt(3))
t.hyp() 
t.angle1() 
t.angle2() 

t2 = RightTriangle(1,1)
t2.hyp()
t2.angle1()
t2.angle2()