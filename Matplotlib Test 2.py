from matplotlib import pyplot as plt
import matplotlib.cm as cm
from LifeGame import LifeGame


def run(lg2):
    for _ in lg2.run(100):
        plt.axis('off')
        plt.imshow(lg2.get_raw(), cmap=plt.cm.viridis) #, interpolation='quadric')
        canvas.draw()
        plt.clf()


lg = LifeGame()

# lg.set_r_pentamino(40, 40)
# lg.set_glider(15, 15)
lg.read_file('glider.txt')
# print(lg)

ax = plt.subplot(111)
canvas = ax.figure.canvas

manager = plt.get_current_fig_manager()
manager.window.after(100, run, lg)
plt.show()

# plt.spy(lg.matrix)
# plt.axis('off')
# plt.show()
# # plt.clf()
#
# for step in lg.run(10):
#     plt.spy(lg.matrix)
#     plt.axis('off')
#     plt.show()
