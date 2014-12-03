# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 20:37:55 2014

@author: yuhao
"""
import numpy as np

# hyperbola
#
def hyperbola(a, b):
    return 1 + np.sqrt(a**2 + 25.0*(b-1)**2)

# matrix multiply and its adjoint
# 
def mat_mult(adj, add, B, x, nx, y, ny):
    for ix in range(nx):
        for iy in range(ny):
            if adj == True:
                x[ix] += B[iy, ix] * y[iy]
            else:
                y[iy] += B[iy, ix] * x[ix]
                
# first derivative one dimension
def igrad1(adj, add, xx, n, yy):
    for i in range(1,n-1,1):
        if adj == False:
            yy[i] = yy[i] + xx[i+1] - xx[i]
        else:
            xx[i+1] = xx[i+1] + yy[i]
            xx[i] = xx[i] - yy[i]
