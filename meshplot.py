# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 11:22:51 2016

@author: Daniel Huang
"""


 


import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up grid and test data. set up co ordinate system
nx, ny =  2047,1000
x = range(nx)
y = range(ny)


v = np.genfromtxt("2Intensities.txt",unpack=True)
m=np.zeros(999)


for i in range(999):
    if i <=4:
        v[:,i]=0

# 3D plot
hf = plt.figure()
ha = hf.add_subplot(111, projection='3d')

X, Y = np.meshgrid(x, y)  
ha.plot_surface(X, Y, v,cmap='coolwarm')#, rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
#plt.ylim(850,1000)
plt.show()
 

 
 
 
 