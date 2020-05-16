# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:43:53 2020

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt

def cantor(n):
    return [0.] + cant(0., 1., n) + [1.]

def cant(x, y, n):
    if n == 0:
        return []

    new_pts = [2.*x/3. + y/3., x/3. + 2.*y/3.]
    return cant(x, new_pts[0], n-1) + new_pts + cant(new_pts[1], y, n-1)

x = np.array(cantor(20))
y = np.cumsum( np.ones(len(x))/(len(x)-2) ) - 1./(len(x)-2)
y[-1] = 1

def cantor_function(x,cant_x,cant_y):
    index=np.argmin(np.abs(x-cant_x))
    return(cant_y[index])
    
def original_exp(x,n):
    prodcos = np.prod(np.cos([x/(3**k) for k in np.arange(1,n,1)]))
    Re = np.cos(x/2)*prodcos
    Im = np.sin(x/2)*prodcos
    return(np.array([Re,Im]))

def estimate_exp(x,samples,cantor_samples):
    sumsin = np.sum(np.multiply(np.sin(x*samples),cantor_samples))
    sumcos = np.sum(np.multiply(np.cos(x*samples),cantor_samples))
    Re = np.cos(x)+(x/len(samples))*sumsin
    Im = np.sin(x)-(x/len(samples))*sumcos
    return(np.array([Re,Im]))

np.random.seed(144)
samples = np.random.uniform(size=100000)
cantor_samples = np.array([cantor_function(k,x,y) for k in samples])

x_range=np.arange(-6,6,0.05)
ori_Re=[0]*len(x_range)
ori_Im=[0]*len(x_range)

for i in range(len(x_range)):
    st=original_exp(x_range[i],100000)
    ori_Re[i]=st[0]
    ori_Im[i]=st[1]
    print(i)
    
    
est_range=np.arange(-6,6,0.25)
est_Re=[0]*len(est_range)
est_Im=[0]*len(est_range)

for i in range(len(est_range)):
    st=estimate_exp(est_range[i],samples,cantor_samples)
    est_Re[i]=st[0]
    est_Im[i]=st[1]
    print(i)
    
x_range_MSE=np.arange(-6,6,0.25)
ori_Re_MSE=[0]*len(x_range_MSE)
ori_Im_MSE=[0]*len(x_range_MSE)

for i in range(len(x_range_MSE)):
    st=original_exp(x_range_MSE[i],100000)
    ori_Re_MSE[i]=st[0]
    ori_Im_MSE[i]=st[1]
    print(i)
    
MSE_Re=np.square(np.subtract(ori_Re_MSE,est_Re)).mean() 
MSE_Im=np.square(np.subtract(ori_Im_MSE,est_Im)).mean() 

fig=plt.figure()
plot_Re=plt.subplot(2,1,1)
plt.plot(x_range,ori_Re)
plt.scatter(est_range,est_Re,marker='o',c='red',s=10)
#plot_Re.plot(x_range,ori_Re,est_range,est_Re,'ro')
plot_Im=plt.subplot(2,1,2)
plt.plot(x_range,ori_Im)
plt.scatter(est_range,est_Im,marker='o',c='red',s=10)
#plot_Im.plot(x_range,ori_Im,est_range,est_Im,'ro')
fig.savefig('F1.pdf')

