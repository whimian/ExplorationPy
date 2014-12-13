# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 15:45:54 2014

@author: yuhao
"""
from raytrace import *

vp = [1500, 2000, 2500, 3000, 3500]
vs = [1500, 1600, 2000, 2250]
rho = [2.3, 2.7, 2.8, 3.0]
thic = [50, 50, 50, 50]
offset = [25, 50, 75, 100, 125]
ppp = raytrace(vp, vs, rho, thic, offset)