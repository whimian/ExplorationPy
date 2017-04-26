import numpy as np
import matplotlib.pyplot as plt


def hyperbola(a, b):
    return 1 + np.sqrt(a**2 + 25.0*(b-1)**2)


def mat_mult(adj, add, B, x, nx, y, ny):
    "matrix multiplication and its joint"
    for ix in xrange(nx):
        for iy in xrange(ny):
            if adj is True:
                x[ix] += B[iy, ix] * y[iy]
            else:
                y[iy] += B[iy, ix] * x[ix]


def igrad1(adj, add, xx, n, yy):
    "1-D first derivative"
    for i in xrange(1, n-1):
        if adj is False:
            yy[i] = yy[i] + xx[i+1] - xx[i]
        else:
            xx[i+1] = xx[i+1] + yy[i]
            xx[i] = xx[i] - yy[i]


def lmo(adj, add, slowness, tau0, t0, dt, x0, dx, modl, nt, nx, data):
    "linear moveout"
    for ix in range(1, nx):
        x = x0 + dx * (ix - 1)
        for it in range(1, nt):
            t = t0 + dt * (it - 1)
            tau = t - x * slowness
            iu = 1.5001 + (tau-tau0)/dt
            if 0 < iu and iu <= nt:
                if adj == 0:
                    data[it, ix] = data[it, ix] + modl[iu, ix]
                else:
                    modl[iu, ix] = modl[iu, ix] + data[it, ix]


def wiggle(Data, SH, skipt=1, maxval=8, lwidth=.1):
    """variable area wiggle trace
    """
    t = range(SH['ns'])
    for i in range(0, SH['ntraces'], skipt):
        trace = Data[:, i]
        trace[0] = 0
        trace[SH['ns'] - 1] = 0
        plt.plot(i + trace/maxval, t, color='black', linewidth=lwidth)
        # pl.gca().invert_yaxis()
        for a in range(len(trace)):
            if trace[a] < 0:
                trace[a] = 0
    # pylab.fill(i+Data[:,i]/maxval,t,color='k',facecolor='g')
    plt.fill(i+Data[:, i]/maxval, t, 'k', linewidth=0)
    plt.title(SH['filename'])
    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.show()


def ricker(dt, fdom, tlength):
    "ricker wavelet"
#    if(nargin<3):
#        tlength=127.*dt
#    if(nargin<2):
#        fdom=15.0
# create a time vector
    nt = np.round(tlength/dt) + 1
    tmin = -1 * dt * np.round(nt / 2)
    # tw=tmin+dt*(0:nt-1)'
    tw = tmin + dt*np.arange(nt)
    # create the wavelet
    pf = np.pi**2 * fdom**2
    wavelet = (1 - 2. * pf * tw**2) * np.exp(-pf * tw**2)
    re = {'tw': tw, 'wavelet': wavelet}
    return re
# normalize
# generate a refenence sinusoid at the dominant frequency
# wavelet=wavenorm(wavelet,tw,2)
