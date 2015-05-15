import numpy as np
# import marine as ma
import matplotlib.pyplot as plt

t = np.r_[0:0.5:1000j]

def heaviside(t):
    return 0.5 * (np.sign(t) + 1)


def ricker(t, fm, tm, R, v):
    k = R/v
    f = heaviside(t - k) * (1 - 2 * np.pi**2 * fm**2 * (t - tm - k)**2) *\
        np.exp(-np.pi**2 * fm**2 * (t - tm - k)**2)
    return f

# w = np.zeros(t.shape)
# for i in range(len(t)):
#     w[i] = ricker(t[i], 30., 0.03, 400., 2000.)

# plt.plot(t, w)

r = np.r_[-500:500:501j]
z = np.r_[0:2000:1001j]
t = np.r_[0:0.6:0.003]
nr = len(r)
nz = len(z)
nt = len(t)

dr = 2
dz = 2
dt = 0.003

A = np.zeros((len(r), len(z), len(t)))
B = np.zeros((len(r), len(z), len(t)))
for p in range(1, nt-1):
    for m in range(1, nr-1):
        for n in range(1, nz-1):
            if (p == 0):
                continue
            else:
                if (n <= 501):
                    vp = 2000
                    vs = 1500
                else:
                    vp = 1500 * 1.1
                    vs = 2000 * 1.1

                if (m != nr/2):
                    A1 = 2 * A[m, n, p]
                    A2 = -A[m, n, p-1]
                    A3 = (vp * dt / dr)**2 * \
                        (A[m+1, n, p] - 2 * A[m, n, p] + A[m-1, n, p])
                    A4 = 0.5 * (vp * dt / dr)**2 / (m - nr/2) * \
                        (A[m+1, n, p] - A[m-1, n, p])
                    A5 = - (vp*dt/dr)**2 / \
                        (m - nr/2)**2 * A[m, n, p]
                    A6 = 0.25 * (vp*dt/dr)**2 * (dr/dz) * (1 - (vs/vp)**2) * \
                        (B[m+1, n+1, p] - B[m+1, n-1, p] -
                            B[m-1, n+1, p] + B[m-1, n-1, p])
                    A7 = (vp*dt/dr)**2 * (dr/dz)**2 * (vs/vp)**2 * \
                        (A[m, n+1, p] - 2 * A[m, n, p] + A[m, n-1, p])
                    A[m, n, p+1] = A1 + A2 + A3 + A4 + A5 + A6 + A7

                    B1 = 2 * B[m, n, p]
                    B2 = -B[m, n, p-1]
                    B3 = (vp * dt / dr)**2 * (dr/dz)**2 * \
                        (B[m, n+1, p] - 2 * B[m, n, p] + B[m, n-1, p])
                    B4 = 0.5 * (vp*dt/dr)**2 * (dr/dz) * (1 - (vs/vp)**2) / \
                        (m - nr/2) * (A[m, n+1, p] - A[m, n-1, p])
                    B5 = 0.25 * (vp*dt/dr)**2 * (dr/dz) * (1 - (vs/vp)**2) * \
                        (A[m+1, n+1, p] - A[m+1, n-1, p] -
                            A[m-1, n+1, p] + A[m-1, n-1, p])
                    B6 = 0.5 * (vp*dt/dr)**2 * (vs/vp)**2 / (m - nr/2) * \
                        (B[m+1, n, p] - B[m-1, n, p])
                    B[m, n, p+1] = B1 + B2 + B3 + B4 + B5 + B6

A[nr/2, :, :] = 0
for p in range(1, nt-1):
    for n in range(1, nz-1):
        B1 = 2 * B[nr/2, n, p]
        B2 = -B[nr/2, n, p-1]
        B3 = (vp*dt/dr)**2 * (dr/dz)**2 * \
            (B[nr/2, n+1, p] - 2 * B[nr/2, n, p] -
                2 * B[nr/2, n, p] + B[nr/2, n-1, p])
        B4 = 1.5 * (vp*dt/dr)**2 * (dr/dz) * (1 - (vs/vp)**2) * \
            (A[nr/2+1, n+1, p] - A[nr/2+1, n-1, p])
        B5 = 2 * (vp*dt/dr)**2 * (vs/vp)**2 * \
            (B[nr/2+1, n, p] - B[nr/2, n, p])
        B[nr/2, n, p+1] = B1 + B2 + B3 + B4 + B5

# A[m, n, p+1] = 2 * A[m, n, p] - A[m, n, p-1] + \
#                        (vp * dt / dr)**2 * \
#                        (A[m+1, n, p] - 2 * A[m, n, p] + A[m-1, n, p]) + \
#                        0.5 * (vp * dt / dr)**2 / (m - nr/2) * \
#                        (A[m+1, n, p] - A[m-1, n, p]) - (vp*dt/dr)**2 / \
#                        (m - nr/2)**2 * A[m, n, p] + 0.25 * (vp*dt/dr)**2 * \
#                        (dr/dz) * (1 - (vs/vp)**2) * \
#                        (B[m+1, n+1, p] - B[m+1, n-1, p] -
#                            B[m-1, n+1, p] + B[m-1, n-1, p]) + \
#                        (vp*dt/dr)**2 * (dr/dz)**2 * (vs/vp)**2 * \
#                        (A[m, n+1, p] - 2 * A[m, n, p] + A[m, n-1, p])
# B[m, n, p+1] = 2 * B[m, n, p] - B[m, n, p-1] + \
#                        (vp * dt / dr)**2 * (dr/dz)**2 * \
#                        (B[m, n+1, p] - 2 * B[m, n, p] + B[m, n-1, p]) + \
#                        0.5 * (vp*dt/dr)**2 * (dr/dz) * (1 - (vs/vp)**2) / \
#                        (m - nr/2) * (A[m, n+1, p] - A[m, n-1, p]) + \
#                        0.25 * (vp*dt/dr)**2 * (dr/dz) * (1 - (vs/vp)**2) * \
#                        (A[m+1, n+1, p] - A[m+1, n-1, p] -
#                            A[m-1, n+1, p] + A[m-1, n-1, p]) + \
#                        0.5 * (vp*dt/dr)**2 * (vs/vp)**2 / (m - nr/2) * \
#                        (B[m+1, n, p] - B[m-1, n, p])
# B[nr/2, n, p+1] = 2 * B[nr/2, n, p] - B[nr/2, n, p-1] + \
#            (vp*dt/dr)**2 * (dr/dz)**2 * \
#            (B[nr/2, n+1, p] - 2 * B[nr/2, n, p] + B[nr/2, n-1, p]) + \
#            1.5 * (vp*dt/dr)**2 * (dr/dz) * (1 - (vs/vp)**2) * \
#            (A[nr/2+1, n+1, p] - A[nr/2+1, n-1, p]) + \
#            2 * (vp*dt/dr)**2 * (vs/vp)**2 * (B[nr/2+1, n, p] - B[nr/2, n, p])
