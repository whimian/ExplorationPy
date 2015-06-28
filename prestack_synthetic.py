# import raytraceClass as rc
import numpy as np
# import matplotlib.pyplot as plt

from raytrace import *
from zoeppritz import *
import marine as ma

vp = np.array([1500, 2000, 2500, 3000, 3500])
vs = np.array([1500, 1600, 2000, 2250, 2000])
rho = np.array([2.3, 2.7, 2.8, 3.0, 3.0])
thic = np.array([50, 50, 50, 50])
offset = np.array([25, 50, 75, 100])

pm, tm = raytrace(vp, thic, offset)

rayParameter = pm

reflec = np.zeros((thic.shape[-1], offset.shape[-1]))

for ii in np.arange(pm.shape[0]):
    for io in np.arange(pm.shape[1]):
        reflec[ii, io] = zoeppritz(vp[ii], vp[ii+1], vs[ii], vs[ii+1],
                                   rho[ii], rho[ii+1], pm[ii, io], 'r')

tw = []
wavelet = []
dt = 0.01
fdom = 30
tlength = 1.0
re = ma.ricker(dt, fdom, tlength)
tw = re['tw']
wavelet = re['wavelet']
W = np.fft.fft(wavelet)
freq = np.fft.fftfreq(tw.shape[-1], d=0.01)

T = np.zeros((freq.shape[-1], offset.shape[-1]), dtype=complex)

for io in np.arange(offset.shape[-1]):
    for f in np.arange(freq.shape[-1]):
        temp = 0
        for ii in np.arange(thic.shape[-1]):
            temp += reflec[ii, io] * W[f] *\
                    np.exp(1j * 2 * np.pi * freq[f] * tm[ii, io])
        T[f, io] = temp

A = np.real(T)
SH = {'ns': freq.shape[-1]/2 + 1, 'ntraces': 4, 'filename': 'abc'}
ma.wiggle(A[0: freq.shape[-1]/2 + 1, :], SH)
