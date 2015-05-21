# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 14:53:12 2014

@author: yuhao
"""
import numpy as np


def zoeppritz(vp1, vp2, vs1, vs2, rho1, rho2, p, flag='r'):
    """
    Compute reflection&refraction coefficient of a given ray(ray parameter)

    Parameters
    ----------
    vp1: compressional wave velocity in upper layer
    vp2: compressional wave velocity in lower layer
    vs1: shear wave velocity in upper layer
    vs2: shear wave velocity in lower layer
    rho1: density of upper layer
    rho2: density of lower layer
    p: ray parameter
    flag: r = reflection, else = refraction

    Returns
    -------
    reflection or refraction coefficient
    """

    # try:
    # raise Exception('LargerThanCriticalError')
    # except:
    # return None
    parameter = []
    sin_critical_angle = p * vp2  # check critical angle
    if sin_critical_angle >= 1:
        parameter = schoenberg_protazaio(vp1, vp2, vs1, vs2,
                                         rho1, rho2, p, flag)
    else:
        parameter = dahl_ursin(vp1, vp2, vs1, vs2, rho1, rho2, p, flag)
    return parameter


def dahl_ursin(vp1, vp2, vs1, vs2, rho1, rho2, p, flag):
    """
        Calculate the reflection and transmision coefficient
        [Dahl and Ursin (1991)]
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
        rho1 * rho2 * (vs1*vp2 * P1 * P4 + vp1 * vs2 * P2 * P3) + \
        vp1 * vs1 * P3 * P4 * Y**2 + \
        vp2 * vs2 * P1 * P2 * X**2 + \
        vp1 * vp2 * vs1 * vs2 * p**2 * Z**2

    Nr = q**2 * p**2 * P1 * P2 * P3 * P4 + \
        rho1 * rho2 * (vs1*vp2*P1*P4 - vp1*vs2*P2*P3) - \
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


def schoenberg_protazaio(vp1, vp2, vs1, vs2, rho1, rho2, p, flag):
    """
    Calculate the reflection and transmision coefficient of P- and S-wave
    [Schoenberg and Protazio (1992)]
    """
    Sp = np.sqrt(vp1**(-2) - p**2)
    Ss = np.sqrt(vs1**(-2) - p**2)
    K = 1 - 2 * vs1**2 * p**2
    x1 = vp1 * p
    x2 = vp1 * Ss
    x3 = -rho1 * vp1 + 2 * rho1 * vs1**3
    x4 = p * Ss
    X = np.matrix([[x1, x2], [x3, x4]])
    y1 = -2 * rho1 * vp1 * vs1**2 * p * Sp
    y2 = -rho1 * vs1 * K
    y3 = vp1 * Sp
    y4 = -vs1 * p
    Y = np.matrix([[y1, y2], [y3, y4]])

    p_ = p * vp1 / vp2
    Sp_ = np.sqrt(vp2**(-2) - p_**2)
    Ss_ = np.sqrt(vs2**(-2) - p_**2)
    K_ = 1 - 2 * vs2**2 * p_**2
    x1_ = vp2 * p_
    x2_ = vp2 * Ss_
    x3_ = -rho2 * vp2 + 2 * rho2 * vs2**3
    x4_ = p_ * Ss_
    X_ = np.matrix([[x1_, x2_], [x3_, x4_]])
    y1_ = -2 * rho2 * vp2 * vs2**2 * p_ * Sp_
    y2_ = -rho2 * vs2 * K_
    y3_ = vp2 * Sp_
    y4_ = -vs2 * p_
    Y_ = np.matrix([[y1_, y2_], [y3_, y4_]])
    T = 2 * Y_.I * (X.I * X_ * Y_.I * Y + K).I
    R = (X.I * X_ * Y_.I * Y + K).I * (X.I * X_ * Y_ * Y - K)
    if flag == 'r':
        return R[0, 0]
    else:
        return T[0, 0]
