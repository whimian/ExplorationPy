# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 20:37:55 2014

@author: yuhao
"""
import numpy as np

def marine_hyperbola(a, b):
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