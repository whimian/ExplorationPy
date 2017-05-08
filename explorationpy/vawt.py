# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 2017
"""
from __future__ import division, print_function, absolute_import

__author__ = "yuhao"

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cspline1d, cspline1d_eval

# class Wtva(object):
#     def __init__(self):
#         self.origin = 0
#         self.posFill = 'black'
#         self.negFill = None
#         self.lineColor = None
#         self.resampleRatio = 10
#         self.rescale = rescale

def wiggle(values, origin=0, posFill='black', negFill=None, lineColor='black',
           resampleRatio=10, rescale=False, zmin=0, zmax=None, ax=None):
    """
    Plot a trace in VAWT(Variable Area Wiggle Trace)

    Parameters
    ----------
    x: input data (1D numpy array)

    origin: (default, 0) value to fill above or below (float)

    posFill: (default, black)
        color to fill positive wiggles with (string or None)

    negFill: (default, None)
        color to fill negative wiggles with (string or None)

    lineColor: (default, black)
        color of wiggle trace (string or None)

    resampleRatio: (default, 10)
        factor to resample traces by before plotting (1 = raw data) (float)

    rescale: (default, False)
        If True, rescale "x" to be between -1 and 1

    zmin: (default, 0)
        The minimum z to use for plotting

    zmax: (default, len(x))
        The maximum z to use for plotting

    ax: (default, current axis)
        The matplotlib axis to plot onto

    Return
    ------
    Plot
    """
    if zmax is None:
        zmax = values.size

    # Rescale so that values ranges from -1 to 1
    if rescale:
        values = values.astype(np.float)
        values -= values.min()
        values /= values.ptp()
        values *= 2
        values -= 1

    # Interpolate at resampleRatio x the previous density
    resample_z = np.linspace(0, values.size, values.size * resampleRatio)
    # cubic spline interpolation
    cj = cspline1d(values)
    resample_v = cspline1d_eval(cj, resample_z)

    # newz = np.linspace(zmax, zmin, resample_z.size)
    # newz = np.linspace(zmin, zmax, resample_z.size)
    newz = resample_z
    if origin == None:
        origin = resample_v.mean()

    # # Plot
    # if ax is None:
    #     ax = plt.gca()
    #     # plt.hold(True)
    if posFill is not None:
        ax.fill_betweenx(newz, resample_v, origin,
                         where=resample_v > origin,
                         facecolor=posFill)
    if negFill is not None:
        ax.fill_betweenx(newz, resample_v, origin,
                         where=resample_v < origin,
                         facecolor=negFill)
    if lineColor is not None:
        ax.plot(resample_v, newz, color=lineColor, linewidth=.1)


def wiggles(data, wiggleInterval=10, overlap=1, posFill='black',
            negFill=None, lineColor='black', rescale=True, extent=None, ax=None):
    """
    2-D Wiggle Trace Variable Amplitude Plot

    Parameters
    ----------
    x: input data (2D numpy array)
    wiggleInterval: (default, 10) Plot 'wiggles' every wiggleInterval traces
    overlap: (default, 0.7) amount to overlap 'wiggles' by (1.0 = scaled
            to wiggleInterval)
    posFill: (default, black) color to fill positive wiggles with (string
            or None)
    negFill: (default, None) color to fill negative wiggles with (string
            or None)
    lineColor: (default, black) color of wiggle trace (string or None)
    resampleRatio: (default, 10) factor to resample traces by before
            plotting (1 = raw data) (float)
    extent: (default, (0, nx, 0, ny)) The extent to use for the plot.
            A 4-tuple of (xmin, xmax, ymin, ymax)
    ax: (default, current axis) The matplotlib axis to plot onto.
    Output:
        a matplotlib plot on the current axes
    """
    # Rescale so that the data ranges from -1 to 1
    if rescale:
        data = data.astype(np.float)
        data -= data.min()
        data /= data.ptp()
        data *= 2
        data -= 1

    if extent is None:
        xmin, ymin = 0, data.shape[0]
        ymax, xmax = 0, data.shape[1]
    else:
        xmin, xmax, ymin, ymax = extent

    if ax is None:
        fig, ax = plt.subplots()
    ax.invert_yaxis()
    ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax]) # xrange should be larger!!!
    ny, nx = data.shape
    x_loc = np.linspace(xmin, xmax, nx)
    for i in range(wiggleInterval//2, nx, wiggleInterval):
        x = overlap * (wiggleInterval / 2.0) * (x_loc[1] - x_loc[0]) * data[:, i]
        wiggle(x + x_loc[i], origin=x_loc[i], posFill=posFill, negFill=negFill,
               lineColor=lineColor, zmin=ymin, zmax=ymax, ax=ax)
