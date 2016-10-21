# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:24:55 2016

@author: Daniel Huang
"""
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


# 

t= np.genfromtxt("1Spec_Latency.txt",unpack=True)
v = np.genfromtxt("1Intensities.txt",unpack=True)
w=np.genfromtxt("1WaveLength.txt",unpack=True)


# remove the first few readings - this is an artefact
w[0]=0
w[1]=0
w[2]=0
w[3]=0



vol= np.genfromtxt("1Voltages.txt",unpack=True)
time = np.genfromtxt("1TimeIndex.txt",unpack=True)
ti= np.genfromtxt("1pwrTimeIndex.txt",unpack=True)
p= np.genfromtxt("1Power.txt",unpack=True)
# convert to microwatts
p=p*1000000

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()


plt.subplot(1,3,1)
plt.plot(time,vol)
plt.xlabel('Time Elapsed(s)')
plt.ylabel('Voltage (V)')
plt.rcParams.update({'font.weight': 'bold'})
plt.title('DAQ Reading', fontweight='bold')



plt.subplot(1,3,2)
plt.plot(ti,p)
plt.xlabel('Time Elapsed(s)')
plt.ylabel('Power (microWatts)')
plt.rcParams.update({'font.weight': 'bold'})
plt.title('Power Reading',fontweight='bold')



# Plot the spectral information layer by layer
m=np.zeros(999)

plt.subplot(1,3,3)
for i in range(999):
    plt.plot(w,v[i,:])
    print(i)
    m[i]=np.max(v[i,:])
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (a.u.)')



plt.tight_layout()

# only use this if time is saved in LATENCY FORM. THis converts it to real time elapsed
time=np.zeros(999)
for l in range(997):
    if l==0:
        time[l]=0
    elif l==999:
        time[l]=np.sum(t)
    else:
        time[l]=t[l+1]+time[l-1]



plt.title('Spectral Output', fontweight='bold')
plt.show()




plt.legend(loc= 'upper right')


