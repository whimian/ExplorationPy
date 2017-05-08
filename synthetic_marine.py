# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 21:17:06 2014

Inspired by Jon Claerbout
"""
from __future__ import division, print_function, absolute_import

__author__ = "yuhao"

import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import matplotlib.cm as cm


from explorationpy.marine import hyperbola
from explorationpy.marine import wiggle
from explorationpy.vawt import wiggles

if __name__ == "__main__":
    nz = 50
    depth = np.zeros(nz)
    ny = 60
    refl = np.zeros((nz,ny))
    nh = 60
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
            for i_z in range(nz):  # add hyperbola
                i_y = (ny - 1 - i_s) + (i_h - 1)  # y = midpoint
                i_y = (i_y + 1) % ny
                i_t = hyperbola(depth[i_z], i_h)
                twt[i_z] = i_t
                tr_data_z[i_z] = refl[i_z, i_y]
            func = interp1d(twt, tr_data_z, fill_value=(0, 0), bounds_error=False)
            tr_data_twt = func(np.arange(0, nt))
            data[:, i_h, i_s] += tr_data_twt

    #plt.imshow(data[:,:,40], cmap = cm.gray)
    #plt.show()
    SH = {'ns':60, 'ntraces':60, 'filename':'abc'}
    k = data[:,:,40]
    # wiggle(data[:,:,40],SH)

    fig, ax = plt.subplots()

    wiggles(data[:, :, 40], wiggleInterval=1, ax=ax)
    plt.show()
