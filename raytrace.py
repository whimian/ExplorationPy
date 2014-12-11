# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 21:06:12 2014

@author: yuhao
"""
import numpy as np

def raytrace(Vp, Vs, rho, thic, offset):
    
    pm = np.zeros((len(thic),len(offset)))
    
    for ii in range(len(thic)): #for each interface    
        for io in range(len(offset)): #for each offset      
            err = offset[io]
            counter = 0
            p0 = np.sqrt(np.pi/4.0) / Vp[0]
            flag = False            
            while err > 0.01* offset[io]:
                y0 = 0                
                for i in range(ii):
                    y0 += (thic(i) * Vp[i] * p0) / (np.sqrt(1 - Vp[i]**2 * p0**2))
                ydelta = offset[io] - y0
                pg = 0 # gradient of p relate to y
                for i in range(ii):
                    pg += (thic(i) * Vp[i]) / ((1 - Vp[i]**2 * p0**2)**(1.5))
                p0 += pg * ydelta # corrected p
                err = np.abs(p0 - offset[io])
                counter += 1
                if counter == 100:
                    flag = True
                    break
            if flag == True:
                pm[ii,io] = np.NaN
            else:
                pm[ii,io] = p0