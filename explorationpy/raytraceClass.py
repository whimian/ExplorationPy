# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 16:13:29 2014

@author: yuhao
"""
import numpy as np

class Raytrace():
    Vp = []
    thic = []
    offset = []
    pm = []
    
    def __inint__(self, Vp, thic, offset):
        self.Vp = Vp
        self.thic = thic
        self.offset = offset
        
    def raytrace(self):
        Vp = self.Vp        
        thic = self.thic
#        rho = self.rho
        offset = self.offset
        
        self.pm = np.zeros((len(thic),len(offset)))
    
        for ii in range(len(thic)): #for each interface    
            for io in range(len(offset)): #for each offset      
                err = offset[io]
                counter = 0
                p0 = np.sin(np.pi/4) / Vp[ii]                      
                flag = False
                while err > 0.01* offset[io]:
                    y0 = 0                
                    for i in range(ii + 1):
                        y0 += (thic[i] * Vp[i] * p0) / np.sqrt(1 - Vp[i]**2 * p0**2)
                    y0 = 2 * y0
                    
                    ydelta = offset[io] - y0
                    
                    pg = 0 # gradient of p relate to y
                    for i in range(ii + 1):
                        pg += (thic[i] * Vp[i]) / ((1 - Vp[i]**2 * p0**2)**(1.5))
                    pg = pg**(-1)
                    pg = 0.5 * pg
                    
                    p0 += pg * ydelta # corrected p
                    
                    y = 0                
                    for i in range(ii + 1):
                        y += (thic[i] * Vp[i] * p0) / np.sqrt(1 - Vp[i]**2 * p0**2)
                    y = 2 * y
                    
                    err = np.abs(y - offset[io])
    
                    counter += 1
                    if counter == 100:
                        flag = True
                        break
                if flag == True:
                    self.pm[ii,io] = np.NaN
                else:
                    self.pm[ii,io] = p0