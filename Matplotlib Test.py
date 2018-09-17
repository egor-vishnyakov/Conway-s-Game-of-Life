# import matplotlib.pyplot as plt
# import numpy as np
#
# X = np.linspace(0,1)
# Y = X**3 - X**2 - 2
#
# XX = [0, 1, 2, 3, 4, 5]
# YY = [0, 2, 4, 6, 8, 9]
#
# plt.plot(XX, YY)
# plt.show()
#
# plt.close()
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cm as cm

import sys
import numpy as np
import time

ax = plt.subplot(111)
canvas = ax.figure.canvas

delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
x, y = np.meshgrid(x, y)
z1 = mlab.bivariate_normal(x, y, 1.0, 1.0, 0.0, 0.0)
z2 = mlab.bivariate_normal(x, y, 1.5, 0.5, 1, 1)
z = z2 - z1  # difference of Gaussians

def run(z):
    fig = plt.gcf()
    for i in range(10):
        plt.imshow(z, interpolation='bilinear', cmap=cm.gray,
                  origin='lower', extent=[-3,3,-3,3])
        canvas.draw()
        plt.clf()
        z**= 2


manager = plt.get_current_fig_manager()
manager.window.after(100, run, z)
plt.show()