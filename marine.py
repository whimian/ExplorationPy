# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 20:37:55 2014

@author: yuhao
"""
import numpy as np
import pylab as pl

# hyperbola
#
def hyperbola(a, b):
    return 1 + np.sqrt(a**2 + 25.0*(b-1)**2)

# matrix multiply and its adjoint
# 
def mat_mult(adj, add, B, x, nx, y, ny):
    for ix in range(nx):
        for iy in range(ny):
            if adj == True:
                x[ix] += B[iy, ix] * y[iy]
            else:
                y[iy] += B[iy, ix] * x[ix]
                
# first derivative one dimension
#
def igrad1(adj, add, xx, n, yy):
    for i in range(1,n-1,1):
        if adj == False:
            yy[i] = yy[i] + xx[i+1] - xx[i]
        else:
            xx[i+1] = xx[i+1] + yy[i]
            xx[i] = xx[i] - yy[i]

# linear moveout
#
def lmo(adj, add, slowness, tau0, t0, dt, x0, dx, modl, nt, nx, data):
    for ix in range(1,nx,1):
        x = x0 + dx * (ix - 1)
        for it in range(1,nt,1):
            t = t0 + dt * (it - 1)
            tau =  t - x * slowness
            iu = 1.5001 + (tau-tau0)/dt
            if 0 < iu and iu <= nt:
                if adj == 0:
                    data[it,ix] = data[it,ix] + modl[iu,ix]
                else:
                    modl[iu,ix] = modl[iu,ix] + data[it,ix]
                    
# variable area wiggle trace    
#
def wiggle(Data,SH,skipt=1,maxval=8,lwidth=.1):
    """
    wiggle(Data,SH)
    """    
    t = range(SH['ns'])
    for i in range(0,SH['ntraces'],skipt):
        trace=Data[:,i]
        trace[0]=0
        trace[SH['ns']-1]=0
        pl.plot(i+trace/maxval,t,color='black',linewidth=lwidth)
        #pl.gca().invert_yaxis()
        for a in range(len(trace)):
            if (trace[a]<0):
                trace[a]=0;
		# pylab.fill(i+Data[:,i]/maxval,t,color='k',facecolor='g')
        pl.fill(i+Data[:,i]/maxval,t,'k',linewidth=0)
    pl.title(SH['filename'])
    pl.grid(True)
    pl.gca().invert_yaxis()
    pl.show()
    
# ricker wavelet
def ricker(dt, fdom, tlength):
#    if(nargin<3):
#        tlength=127.*dt
#    if(nargin<2):
#        fdom=15.0
# create a time vector
    nt = np.round(tlength/dt) + 1
    tmin= -dt * np.round(nt/2)
    #tw=tmin+dt*(0:nt-1)'
    tw = tmin + dt*np.arange(nt)
# create the wavelet
    pf=np.pi**2*fdom**2;
    wavelet=(1-2.*pf*tw**2)*np.exp(-pf*tw**2)
    
    re = {'tw':tw, 'wavelet':wavelet}
    return re
# normalize
# generate a refenence sinusoid at the dominant frequency
#wavelet=wavenorm(wavelet,tw,2);