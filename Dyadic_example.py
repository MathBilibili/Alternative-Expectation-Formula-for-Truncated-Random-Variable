# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:00:57 2020

@author: Yang Liu
"""

import numpy as np
import matplotlib.pyplot as plt

def num2dyadic(u, nmax=1024):
    out = np.zeros(nmax)
    i , j = 0 , 0
    while u>0 and i<nmax:
        j = 1 + np.max([0,np.floor(-np.log2(u*(1+np.finfo(float).eps**0.5)))])
        j = int(j)
        if i+j <= nmax:
            i = i+j
            out[i-1] = 1
            u = 2**j*u - 1
        else:
            i = nmax
    return(out[0:i])
    

def Sing(x,a):
    xx = num2dyadic(x)
    N = int(sum(xx))
    ind = np.where(xx==1)[0]+1
    re = 0
    for i in range(N):
        re += a**(ind[i]-i)*(1-a)**(i)
    return(re)

a = 0.15
    
sto = np.zeros(10000)
np.random.seed(144)
runi = np.random.uniform(size=10000)
for i in range(10000):
    sto[i] = Sing(runi[i],a)
Est1 = 1-np.mean(sto)

X1 = np.append(np.arange(0, 1, 0.00001)[1:],0.99999999999999999999999)
Y1 = []
for i in range(len(X1)):
    Y1.append( Sing(X1[i],a) )
    
a = 0.85
    
sto = np.zeros(10000)
np.random.seed(114)
runi = np.random.uniform(size=10000)
for i in range(10000):
    sto[i] = Sing(runi[i],a)
Est2 = 1-np.mean(sto)

X2 = np.append(0.000000000000000000001,np.arange(0, 1, 0.00001)[1:])
Y2 = []
for i in range(len(X2)):
    Y2.append( Sing(X2[i],a) )
    
a = 0.5
    
sto = np.zeros(10000)
np.random.seed(114)
runi = np.random.uniform(size=10000)
for i in range(10000):
    sto[i] = Sing(runi[i],a)
Est3 = 1-np.mean(sto)

X3 = np.arange(0, 1, 0.00001)[1:]
Y3 = []
for i in range(len(X3)):
    Y3.append( Sing(X3[i],a) )
    

fig=plt.figure()
plt.plot(X1,Y1,'r',X2,Y2,'b',X3,Y3,'y')
plt.axvline(x=Est1,c='r',linestyle='--')
plt.axvline(x=Est2,c='b',linestyle='--')
plt.axvline(x=Est3,c='y',linestyle='--')
