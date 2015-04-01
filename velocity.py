# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 21:57:35 2015

@author: yuhao
"""

import numpy as np


def rms2int(twt, v_rms):   
    if len(twt) != len(v_rms):
        raise Exception("Length Mismatch")
    elif len(twt) == 0 or len(v_rms) == 0:
        raise Exception("Zero Length")
    elif False:
        raise Exception("Negative Value")
    else:
        v_int = np.zeros(v_rms.shape)
        v_int[0] = v_rms[0]
        for i in range(1,len(twt)):
            v_int[i] = ((v_rms[i]**2 * twt[i] - v_rms[i-1]**2 * twt[i-1]) / 
                        (twt[i]-twt[i-1]))**0.5
        return v_int


def int2rms(twt, v_int):
    v_rms = []    
    return v_rms


def int2ave(twt, v_int):
    v_ave = []
    return v_ave
