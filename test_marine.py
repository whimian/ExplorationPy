# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 16:53:04 2014

@author: yuhao
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import marine as ma
import raytrace 
adj = False
add = True
B = np.r_[1:9:9j]
B = B.reshape((3,3))
x = np.r_[1:1:3j]
nx = 3
y = np.zeros(3)
ny = 3

ma.mat_mult(adj, add, B, x, nx, y, ny)

tw = []
wavelet = []
dt = 0.01
fdom = 30
tlength = 1.0
re = ma.ricker(dt, fdom, tlength)
tw = re['tw']
wavelet = re['wavelet']

t = np.arange(0,30,0.01)
plt.plot(t, np.sin(2*t))
plt.show()
#spp = np.fft.fft(np.sin(2*t))
#freq = np.fft.fftfreq(t.shape[-1])
#plt.plot(freq, spp.real)#, freq, spp.imag
#plt.show()