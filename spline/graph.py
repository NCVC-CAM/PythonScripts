import numpy as np
import fileinput
import matplotlib.pyplot as plt

dx, dy = np.loadtxt(fileinput.input(), delimiter=',', unpack=True)
qx, qy, w = np.loadtxt("hanako_outline_ctrl.txt", unpack=True)
#fx, fy = np.loadtxt("fit2.txt", unpack=True)

plt.plot(dx, dy, c='k')
#plt.plot(qx, qy, 'o')
#plt.plot(fx, fy, 's')

plt.show()
