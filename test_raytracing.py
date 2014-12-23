# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 15:45:54 2014

@author: yuhao
"""
from raytrace import *
#import raytraceClass as rc
import numpy as np
import zoeppritz as z
vp = [1500, 2000, 2500, 3000, 3500]
#3vp = [1500, 2000]
#vs = [1500, 1600, 2000, 2250]
#rho = [2.3, 2.7, 2.8, 3.0]
thic = [50, 50, 50, 50]
#thic = [50]
offset = [25, 50, 75, 100, 125]
#offset = [50, 100, 150, 200, 250]
#offset = np.arange(1000, 3000, 100)
#zp=[200, 100, 150, 300, 250, 700, 800, 1000, 500]
#vp=[1500, 1600, 2000, 2250, 2700, 2100, 3200, 3750, 4000, 4200]
ppp, ttt = raytrace(vp, thic, offset)

#a = rc.Raytrace()
#a.offset = offset
#a.Vp = vp
#a.thic = thic
#a.raytrace()
#kkk = a.pm
vp1 = 1500
vp2 = 2000
vs1 = 1000
vs2 = 1300
rho1 = 1300
rho2 = 1400
p = np.sin(np.pi / 6.) / 1500.
#p = np.sin(np.pi / 18.) / 1500.
a, b = z.zoeppritz(vp1, vp2, vs1, vs2, rho1, rho2, p)
