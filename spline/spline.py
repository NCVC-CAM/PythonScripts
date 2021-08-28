import numpy as np

def baseN(i, m, t, nv):
    if m == 1:
        if nv[i] <= t < nv[i+1]:
            return 1.0
        else:
            return 0.0
    b = nv[i+m-1] - nv[i]
    if b != 0:
        w1 = (t-nv[i]) / b * baseN(i, m-1, t, nv)
    else:
        w1 = 0
    b = nv[i+m] - nv[i+1]
    if  b != 0:
        w2 = (nv[i+m]-t) / b * baseN(i+1, m-1, t, nv)
    else:
        w2 = 0
    return w1+w2


lqx, lqy, lw = np.loadtxt("q6.txt", unpack=True)
nv = np.loadtxt("nv2.txt")
tmin = min(nv)
tmax = max(nv)

px = []
py = []
for t in np.linspace(tmin, tmax, 100):
    i = 0
    x = 0
    y = 0
    if t==tmax:
        t -= 0.001
    for qx, qy, w in zip(lqx, lqy, lw):
        r = baseN(i, 4, t, nv)
        x += qx * r * w
        y += qy * r * w
        i += 1
    if x!=0 or y!=0:
        px.append(x)
        py.append(y)

for x, y in zip(px, py):
    print(str(x)+','+str(y))
