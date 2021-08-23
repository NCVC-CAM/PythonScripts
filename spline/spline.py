import numpy as np

def baseN(i, m, t, nv):
    if m == 1:
        if nv[i] <= t <= nv[i+1]:
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


lqx, lqy = np.loadtxt("q.txt", unpack=True)
nv = np.loadtxt("nv.txt")

px = []
py = []
for t in range(40):
    i = 0
    x = 0
    y = 0
    for qx, qy in zip(lqx, lqy):
        r = baseN(i, 4, t/10.0, nv)
        x += qx * r
        y += qy * r
        i += 1
    if x != 0:
        px.append(x)
    if y != 0:
        py.append(y)

for x, y in zip(px, py):
    print(str(x)+','+str(y))
