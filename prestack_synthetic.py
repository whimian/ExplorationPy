# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 19:21:10 2014

@author: yuhao
"""
import raytraceClass as rc

vp = [1500, 2000, 2500, 3000, 3500]
vs = [1500, 1600, 2000, 2250, 2000]
rho = [2.3, 2.7, 2.8, 3.0]
thic = [50, 50, 50, 50]
offset = [25, 50, 75, 100, 125]

a = rc.Raytrace()
a.offset = offset
a.Vp = vp
a.thic = thic
a.raytrace()

rayParameter = a.pm

rayParameter[0,:]