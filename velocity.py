# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 21:57:35 2015

@author: yuhao
"""

import numpy as np


class InputError(Exception):
    pass


class LengthMismatchError(InputError):
    def __init__(self, len_1, len_2):
        self.len_1 = len_1
        self.len_2 = len_2

    def __str__(self):
        return 'Warning: The Length of input arrays are mismatched: ' +\
            str(self.len_1) + ' and '+str(self.len_2)


class ZeroLengthError(InputError):
    def __init__(self):
        pass

    def __str__(self):
        return "Warining: One or more input array length are zero!"


class NegativeValueError(InputError):
    def __init__(self):
        pass

    def __str__(self):
        return "Warning: Negative values in input array."


def rms2int(twt, v_rms):
    """Dix Equation"""
    try:
        if len(twt) != len(v_rms):
            raise LengthMismatchError(len(twt), len(v_rms))
        elif len(twt) == 0 or len(v_rms) == 0:
            raise ZeroLengthError
        elif False:
            raise NegativeValueError
        else:
            v_int = np.zeros(v_rms.shape)
            v_int[0] = v_rms[0]
            for i in range(1, len(twt)):
                v_int[i] = ((v_rms[i]**2 * twt[i] -
                            v_rms[i-1]**2 * twt[i-1]) /
                            (twt[i]-twt[i-1]))**0.5
            return v_int
    except LengthMismatchError, e:
        print e.__str__()
        return None
    except ZeroLengthError, e:
        print e.__str__()
        return None


def int2rms(twt, v_int):
    try:
        if len(twt) != len(v_int):
            raise LengthMismatchError(len(twt), len(v_int))
        elif len(twt) == 0 or len(v_int) == 0:
            raise ZeroLengthError
        elif False:
            raise NegativeValueError
        else:
            v_rms = np.zeros(v_int.shape)
            v_rms[0] = v_int[0]
            for i in range(1, len(twt)):
                v_rms[i] = ((v_rms[i-1]**2 * twt[i-1] +
                            v_int[i]**2 * (twt[i] - twt[i-1])) /
                            twt[i])**0.5
            return v_rms
    except LengthMismatchError, e:
        print e.__str__()
        return None
    except ZeroLengthError, e:
        print e.__str__()
        return None


def int2ave(twt, v_int):
    v_ave = []
    return v_ave


if __name__ == '__main__':
    twt = np.array([2, 4, 6])
    v_rms = np.array([1500, 1800])
#    twt = np.array([])
#    v_rms = np.array([])
    v_int = rms2int(twt, v_rms)
