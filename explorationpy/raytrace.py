# -*- coding: utf-8 -*-
"""
Created in 2014
Modifed on Apr. 26th 2017
"""
import numpy as np

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
    m = len(thickness)
    n = len(offset)
    pm = np.zeros((m, n))
    tm = np.zeros((m, n))
    for ii in range(m):  # for each interface
        for io in range(n):  # for each offset
            err = offset[io]
            counter = 0
            p0 = np.sin(np.pi/4) / velocity[ii]
            flag = False
            while err > 0.01 * offset[io]:
                # deviation from target using p0
                y0 = 0
                for i in range(ii + 1):
                    y0 += (thickness[i] * velocity[i] * p0) / np.sqrt(1 - velocity[i]**2 * p0**2)
                y0 = 2 * y0
                ydelta = offset[io] - y0
                # correct p0
                pg = 0  # gradient of p relate to y
                for i in range(ii + 1):
                    pg += (thickness[i] * velocity[i]) / ((1 - velocity[i]**2 * p0**2)**(1.5))
                pg = pg**(-1)
                pg = 0.5 * pg
                p0 += pg * ydelta  # corrected p
                # calculate error for new p0
                y = 0
                for i in range(ii + 1):
                    y += (thickness[i] * velocity[i] * p0) / np.sqrt(1 - velocity[i]**2 * p0**2)
                y = 2 * y
                err = np.abs(y - offset[io])
                # break when correct for 100 times
                counter += 1
                if counter == 100:
                    p0 = np.nan
                    break
            pm[ii, io] = p0
    # Calculate Travel time along specific trace
    for ii in range(m):  # for each interface
        for io in range(n):  # for each offset
            traveltime = 0
            p = pm[ii, io]
            for i in range(ii + 1):
                traveltime = traveltime + 2 * thickness[i] /\
                             (velocity[i] * np.sqrt(1 - velocity[i]**2 * p**2))
            tm[ii, io] = traveltime

    return pm, tm
