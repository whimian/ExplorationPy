# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 16:53:04 2014

@author: yuhao
"""

import numpy as np

from marine import *

adj = False
add = True
B = np.r_[1:9:9j]
B = B.reshape((3,3))
x = np.r_[1:1:3j]
nx = 3
y = np.zeros(3)
ny = 3

mat_mult(adj, add, B, x, nx, y, ny)