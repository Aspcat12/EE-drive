# %%
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
from numpy import sqrt, sin, cos ,pi

## a,b,c ---> alpaha,beta,zero (clarke transform)
def cal_clarke(a, b, c):
    
    alpha = 2/3 * (a - 1/2 * (b + c))
    beta = 2/3 * (sqrt(3)/2 * (b - c))
    zero = 2/3 * 1/2 * (a + b + c)
    
    return alpha, beta, zero

## theta,alpha,beta ---> d,q (park transform)
def cal_park(theta, alpha, beta):
    
    d = cos(theta) * alpha + sin(theta) * beta
    q = -sin(theta) * alpha + cos(theta) * beta
    
    return d, q

## input
ωt = np.arange(0, 4*pi, 0.01)    # start,stop,step (from 0 ---> 4*pi)
a = cos(ωt)
b = cos(ωt-2*pi/3)
c = cos(ωt+2*pi/3)
## input for theta in order to find dq (park transform)
theta=ωt

## Figure 1 = Graph for a,b,c 
fig1,ax1=plt.subplots(figsize=(20,10))
## from string formatter function for x-axis below, I intentionally add pi as text to x-axis value So pi is need to remove from ωt first
ax1.plot(ωt/pi, a, color='red') # a = red color plot
ax1.plot(ωt/pi, b, color='blue') # b = blue color plot
ax1.plot(ωt/pi, c, color='black') # c = black color plot
ax1.grid(True)
## string formatter function for x-axis to simply add text pi to x-axis
ax1.xaxis.set_major_formatter(tck.FormatStrFormatter('%.3g$\pi$'))
## scale number = 1/3
ax1.xaxis.set_major_locator(tck.MultipleLocator(1/3))

## Figure 2 = Graph for Clarke transform
fig2,ax2=plt.subplots(figsize=(20,10))
alpha,beta,zero = cal_clarke(a,b,c) 
ax2.plot(ωt/pi, alpha, color='red') # alpha = red color plot
ax2.plot(ωt/pi, beta, color='blue') # beta = blue color plot
ax2.grid(True)
ax2.xaxis.set_major_formatter(tck.FormatStrFormatter('%.3g$\pi$'))
ax2.xaxis.set_major_locator(tck.MultipleLocator(1/3))

## Figure 3 = Graph for Park transform
fig3,ax3=plt.subplots(figsize=(20,10))
d,q = cal_park(theta,alpha,beta)
ax3.plot(ωt/pi, d, color='red') # d = red color plot
ax3.plot(ωt/pi, q, color='blue') # q = blue color plot
ax3.grid(True)
ax3.xaxis.set_major_formatter(tck.FormatStrFormatter('%.3g$\pi$'))
ax3.xaxis.set_major_locator(tck.MultipleLocator(1/3))


plt.show()


