# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:07:53 2015

@author: yuhao
"""

import numpy as np
import matplotlib.pyplot as plt
from zoeppritz import zoeppritz as zo


def zApp(*args, **kwargs):
    vp1 = kwargs['vp1']
    vp2 = kwargs['vp2']
    vs1 = kwargs['vs1']
    vs2 = kwargs['vs2']
    rho1 = kwargs['rho1']
    rho2 = kwargs['rho2']
    flag = kwargs['flag']
    angle = np.linspace(0, np.pi/2.0, 30)
    p = np.zeros(angle.shape)
    for i in range(0, angle.shape[0]):
        p[i] = np.sin(angle[i])/vp1
    co = np.zeros(angle.shape)
    for i in range(0, angle.shape[0]):
        co[i] = zo(vp1, vp2, vs1, vs2, rho1, rho2, p[i], flag)
    ra = np.linspace(0, 90, 30)
    plt.plot(ra, co)
    plt.xlim((0, 90))
    plt.ylim((0, 1.0))
    plt.show()
    plt.savefig('result')
    return co

if __name__ == '__main__':
#    parameter = {'vp1': 1500, 'vp2': 2000, 'vs1': 1500,
#                 'vs2': 1600, 'rho1': 2.3, 'rho2': 2.7,
#                 'flag': 'r'}

    coefficient = zApp(vp1=1500, vp2=2000, vs1=1500,
                       vs2=1600, rho1=2.3, rho2=2.7, flag='r')
