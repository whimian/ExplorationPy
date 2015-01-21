# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 14:53:12 2014

@author: yuhao
"""

def zoeppritz(vp1, vp2, vs1, vs2, rho1, rho2, p, flag):
    """
    vp1: compressional wave velocity in upper layer
    vp2: compressional wave velocity in lower layer
    vs1: shear wave velocity in upper layer 
    vs2: shear wave velocity in lower layer
    rho1: density of upper layer
    rho2: density of lower layer
    p: ray parameter    
    """
    q = 2 * (rho2 * vs2**2 - rho1 * vs1**2)
    X = rho2 - q * p**2
    Y = rho1 + q * p**2
    Z = rho2 - rho1 - q * p**2
    P1 = (1 - vp1**2 * p**2)**0.5
    P2 = (1 - vs1**2 * p**2)**0.5
    P3 = (1 - vp2**2 * p**2)**0.5
    P4 = (1 - vs2**2 * p**2)**0.5
    
    D = q**2 * p**2 * P1 * P2 * P3 * P4 + \
        rho1 * rho2 *(vs1*vp2*P1*P4 + vp1*vs2*P2*P3) + \
        vp1 * vs1 * P3 * P4 * Y**2 + \
        vp2 * vs2 * P1 * P2 * X**2 + \
        vp1 * vp2 * vs1 * vs2 * p**2 * Z**2
    
    
    Nr = q**2 * p**2 * P1 * P2 * P3 * P4 + \
        rho1 * rho2 *(vs1*vp2*P1*P4 - vp1*vs2*P2*P3) - \
        vp1 * vs1 * P3 * P4 * Y**2 + \
        vp2 * vs2 * P1 * P2 * X**2 - \
        vp1 * vp2 * vs1 * vs2 * p**2 * Z**2
        
    Nt = 2 * vp1 * rho1 * P1 * (vs2 * P2 * X + vs1 * P4 * Y)
    
    rpp = Nr / D
    
    tpp = Nt / D
    if flag == 'r':
        return rpp
    else:
        return tpp