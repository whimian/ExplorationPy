# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 20:37:55 2014

@author: yuhao
"""
import numpy as np

def marine_hyperbola(a, b):
    return 1 + np.sqrt(a**2 + 25.0*(b-1)**2)