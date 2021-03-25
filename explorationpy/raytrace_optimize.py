# -*- coding: utf-8 -*-
"""
Created on Apr. 26th 2017
"""
from functools import partial

import numpy as np
from scipy.optimize import minimize

__author__ = "yuhao"

def raytrace(velocity, thickness, offset):
    """
    Raytracing for simple 1-D VTI model.

    Calculate reflection coefficient and travel time for each interface given
    layer thickness and offset distances.

    Parameters
    ----------
    velocity : 1-d ndarray
        Velocity of each layer

    thickness : 1-d ndarray
        Thickness of each layer

    offset : 1-d ndarray
        Offset positions to be calculated in horizontal direction

    Return
    ------
    pm : 2-d ndarray
        Reflection coefficients for each layer and each offset

    tm : 2-d ndarray
        Travel time for each layer and each offset
    """
    velocity = np.array(velocity)
    thickness = np.array(thickness)
    m = len(thickness)
    n = len(offset)
    pm = np.zeros((m, n))
    tm = np.zeros((m, n))
    for ii in range(m):  # for each interface
        for io in range(n):  # for each offset
            err = offset[io]
            counter = 0
            p0 = np.sin(np.pi/4) / velocity[ii]
            tolerance = 0.01 * offset[io]
            func = partial(
                func_offset, y1=offset[io], velocity=velocity[:ii+1],
                thickness=thickness[:ii+1])
            res = minimize(func, p0, method='Nelder-Mead')
            p0 = res.x[0]
            pm[ii, io] = p0
    # Calculate Travel time along specific trace
    for ii in range(m):  # for each interface
        for io in range(n):  # for each offset
            traveltime = 0
            p = pm[ii, io]
            traveltime = func_traveltime(p, velocity[:ii+1], thickness[:ii+1])
            tm[ii, io] = traveltime

    return pm, tm


def func_traveltime(p, velocity, thickness):
    return np.sum(2 * thickness / (velocity * np.sqrt(1 - velocity**2 * p**2)))


def func_offset(p, y1, velocity, thickness):
    """
    Calculate offset with reflection coefficient p
    """
    offset = 2 * np.sum((thickness * velocity * p) / \
        np.sqrt(1 - velocity**2 * p**2))
    return np.abs(offset - y1)
