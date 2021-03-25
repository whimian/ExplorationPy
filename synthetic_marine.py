# -*- coding: utf-8 -*-
"""
A random jumble of point scatters in a constant-velocity medium.

from Imaging the Earth Interior by Claerbout

Created on Sat Nov 29 21:17:06 2014
"""
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from explorationpy.marine import wiggle
from explorationpy.vawt import wiggles
from explorationpy.vawt import Wiggles

__author__ = "yuhao"

def hyperbola(depth, cdp, trace_interval=25.0):
    """
    travel time index given a constant velocity
    """
    return np.sqrt(depth**2 + trace_interval*cdp**2)


if __name__ == "__main__":
    nz = 50
    depth = np.zeros(nz)
    ny = 60
    refl = np.zeros((nz,ny))
    nh = 30
    nt = 60
    ns = ny
    data = np.zeros((nt, nh, ny))

    for i_z in range(nz):
        depth[i_z] = sp.random.uniform(0, 1.0) * nt  # reflector depth
        layer = 2.0 * sp.random.uniform(0, 1.0) - 1.0  # reflector strength
        refl[i_z, :] = (sp.random.uniform(0, 1.0) + 1) * layer  # texture on layer

    for i_s in range(ny):  # shots
        for i_h in range(nh):  # down cable h = (g-s)/2
            twt = np.zeros((nz,))
            tr_data_z = np.zeros_like(twt)
            i_y = (ns - i_s) + (i_h)  # y = midpoint
            i_y = i_y - ny * (i_y // ny)  # periodic with midpoint
            for i_z in range(nz):  # add hyperbola
                i_t = hyperbola(depth[i_z], i_h)
                twt[i_z] = i_t
                tr_data_z[i_z] = refl[i_z, i_y]
            func = interp1d(twt, tr_data_z, fill_value=(0, 0), bounds_error=False)
            tr_data_twt = func(np.arange(0, nt))
            data[:, i_h, i_s] += tr_data_twt

    # SH = {'ns':60, 'ntraces':60, 'filename':'abc'}
    # k = data[:, :, 40]
    # # wiggle(data[:,:,40],SH)

    fig, ax = plt.subplots()

    wiggles(data[:, :, 40], wiggleInterval=1, ax=ax)
    # vawt = Wiggles(data[:, :, 40])
    # vawt.wiggleInterval = 1
    # vawt.ax = ax
    # vawt.wiggles()
    plt.show()
