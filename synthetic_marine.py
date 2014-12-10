# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 21:17:06 2014
Inspired by Jon Claerbout
@author: yuhao
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from marine import hyperbola
from marine import wiggle

nz = 50
depth = np.zeros(nz)
ny = 60
refl = np.zeros((nz,ny))
nh = 60
nt = 60
ns = ny
data = np.zeros((nt, nh, ny))

for i_z in range(nz):
    depth[i_z] = sp.random.uniform(0, 1.0) * nt  #reflector depth
    layer = 2.0 * sp.random.uniform(0, 1.0) - 1.0 #reflector strength
    for i_y in range(ny):
        refl[i_z,i_y] = (sp.random.uniform(0, 1.0) + 1) * layer #texture on layer

for i_s in range(ny): #shots
    for i_h in range(nh): #down cable h = (g-s)/2
        """for i_t in range(nt):
            data[i_t] = 0"""
        for i_z in range(nz): #add hyperbola
            i_y = (ny -1 -i_s) + (i_h - 1) #y = midpoint
            i_y = (i_y + 1) % ny
#            i_t = 1 + np.sqrt(depth[i_z]**2 + 25.0*(i_h-1)**2)
            i_t = hyperbola(depth[i_z], i_h)
            if i_t < nt:
                data[i_t,i_h,i_s] = data[i_t,i_h,i_s] + refl[i_z,i_y]
#plt.imshow(data[:,:,40], cmap = cm.gray)
#plt.show()
SH = {'ns':60, 'ntraces':60, 'filename':'abc'}
k = data[:,:,40]
wiggle(data[:,:,40],SH)