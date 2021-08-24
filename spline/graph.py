import numpy as np
import fileinput
import matplotlib.pyplot as plt

dx, dy = np.loadtxt(fileinput.input(), delimiter=',', unpack=True)
qx, qy = np.loadtxt("q.txt", unpack=True)

plt.plot(dx, dy, c='k')
plt.plot(qx, qy, 'o')

plt.show()
