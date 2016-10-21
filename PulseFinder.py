# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 16:02:47 2016

@author: Daniel Huang
"""


import numpy as np
import matplotlib.pyplot as plt
from functools import wraps
##############################################################
''' This function is defined so that subsquent calculations (via the 'find' function) are only run once per cycle
'''
def run_once(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            result = f(*args, **kwargs)
            wrapper.has_run = True
            return result
    wrapper.has_run = False
    return wrapper

@run_once
def load_ipython_extension(ip):
    pass
##############################################################


# This is the forwards version of the 'find' function. See notes below the function for when to use the reverse version.
def find(start,end): 
    # first find the maximum amplitude of the current sub pulse     
    print('maximum is', np.max(v))   
    # find 10% of max amplitude
    value=0.1*np.max(v)
    # create a horizontal line at 10% of max amplitude
    ten=np.zeros(np.size(time))
    for a in range(np.size(time)):
        ten[a]=value
    
    # find the index at which the data set is closest to the index at 10% of max amplitude
    difference=np.zeros(np.size(time))
    for b in range(np.size(time)):
        difference[b]= np.abs(v[b]-value)
    
    intercept=np.min(difference)
    

    inter1=0
    for c in range(np.size(time)):        
        if difference[c]==intercept:
            inter1=c
            print('intersect index 1 is at', inter1)
    peak=np.max(v)        
    for h in range(np.size(v)):
        if v[h]==peak:
            peakisat=h

    # now find the other index
    difference2=np.ones((peakisat))        
    for d in range((peakisat-1)):
        difference2[d]= np.abs(v[d]-value)
        
        
    intercept2=np.min(difference2)
    
    inter2=0
    for e in range((peakisat-1)):        
        if difference2[e]==intercept2:
            inter2=e
            print('intersect index 2 is at', inter2)
    # the difference between the 2 indices is t0.1
    result=np.abs(inter2-inter1)/100
    print('Pulse duration is', result, 'ms')
    #return (np.abs(inter2-inter1))
    return result
##############################################################

# Important note: the function above assumes the first intersect (of the 10% max amplitude) will be on the decaying side of the pulse, which will be the case most of the time.
# If the first intersect is in fact on the rising phase of the pulse, please use the modified version of the 'find' function instead and comment out the function above.
# This will be necessary if the output of one or more pulse states "Pulse duration is 0.0ms"    
'''
# This is the reverse version of the 'find' function. See notes above for when to use the forwards version
def find(start,end): 

    print('maximum is', np.max(v))
    value=0.1*np.max(v)
    ten=np.zeros(np.size(time))
    for a in range(np.size(time)):
        ten[a]=value
    
    
    plt.scatter(time,ten)

    difference=np.zeros(np.size(time))
    for b in range(np.size(time)):
        difference[b]= np.abs(v[b]-value)
    
    intercept=np.min(difference)
    

    inter1=0
    for c in range(np.size(time)):        
        if difference[c]==intercept:
            inter1=c
            print('intersect index 1 is at', inter1)
    peak=np.max(v)        
    for h in range(np.size(v)):
        if v[h]==peak:
            peakisat=h
            
    
#############################
#############################    
    
    # now find the other index
    difference2=np.ones((200000))        

    for d in range((199999)):
        if d <= peakisat:
            v[d]=0
            
        difference2[d]= np.abs(v[d]-value)
   
    intercept2=np.min(difference2)
    inter2=0
    for e in range((199999)):        
        if difference2[e]==intercept2:
            inter2=e
            print('intersect index 2 is at', inter2)
    result=np.abs(inter2-inter1)/100
    print('Pulse duration is', result, 'ms')
    #return (np.abs(inter2-inter1))
    return result
'''


##############################################################

# Import the IPL data files. Note hdf5 files can easily be converted into text files
time = np.genfromtxt("3TimeIndex.txt",unpack=True)
v = np.genfromtxt("3Voltages.txt",unpack=True)

# plot to see the general trend

plt.scatter(time,v)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('DAQ Reading')
plt.legend(loc= 'upper right')


# find the average background voltage from the first few data values, assuming this is a good representation of the background level

firstfew = np.zeros(1000)
for i in range(1000):
    firstfew[i]=v[i]

background=np.average(firstfew)

#print('Background level is', background, 'V')

################################################################    

''' 
From observing the data, define a starting and ending point of sub pulses to make analysis quicker.
Please manually edit to custom - define where to start.

note the sampling rate is 100 000Hz and runs for 2 seconds, so 100 000 * 1.414 as in this example will start at 1.414s
 '''
start=100000*1.414
end=100000*1.424

action = run_once(find)

# the following code separates the whole data file into smaller sections, one for each sub pulse
# I acknolegdge that this is a somewhat crude method, but it does yield consistent results.

# define region of one subpulse
for subpulse in range(6):
    if subpulse ==0:
        for ab in range(199999):
            if ab<=start:
                v[ab]=0
            elif ab>=end:
                v[ab]=0   
            #elif ab==199997:
        find(start,end)
            
###############################
    elif subpulse ==1:
        v = np.genfromtxt("3Voltages.txt",unpack=True)
        start=start+1625
        end =end+1625
        
        for ab in range(199999):
            if ab<=start:
                v[ab]=0
            elif ab>=end:
                v[ab]=0
        action.has_run = False  
        find(start,end)        
###############################
    elif subpulse ==2:
        v = np.genfromtxt("3Voltages.txt",unpack=True)
        start=start+1600
        end =end+1600
        
        for ab in range(199999):
            if ab<=start:
                v[ab]=0
            elif ab>=end:
                v[ab]=0
        action.has_run = False  
        find(start,end)     
###############################   
    elif subpulse ==3:
        v = np.genfromtxt("3Voltages.txt",unpack=True)
        start=start+1625
        end =end+1625
        
        for ab in range(199999):
            if ab<=start:
                v[ab]=0
            elif ab>=end:
                v[ab]=0
        action.has_run = False  
        find(start,end)     
###############################    
    elif subpulse ==4:
        v = np.genfromtxt("3Voltages.txt",unpack=True)
        start=start+1625
        end =end+1625
        
        for ab in range(199999):
            if ab<=start:
                v[ab]=0
            elif ab>=end:
                v[ab]=0
        action.has_run = False  
        find(start,end)     
###############################
    elif subpulse ==5:
        v = np.genfromtxt("3Voltages.txt",unpack=True)
        start=start+1625
        end =end+1625
        
        for ab in range(199999):
            if ab<=start:
                v[ab]=0
            elif ab>=end:
                v[ab]=0
        action.has_run = False  
        find(start,end)     
##############################################




