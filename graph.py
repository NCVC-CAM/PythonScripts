import numpy as np
import fileinput
import matplotlib.pyplot as plt

dx, dy = np.loadtxt(fileinput.input(), delimiter=',', unpack=True)

plt.plot(dx, dy, c='k')
plt.axhline(0, linewidth=2)
plt.axvline(0, linewidth=2)

plt.show()
