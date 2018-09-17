from matplotlib import pyplot as plt
import matplotlib.cm as cm
from LifeGame import LifeGame

lg = LifeGame()

# This is glider
# lg.append_line((False, True, False, False, False, False, False, False, False, False, False))
# lg.append_line((False, False, True, False, False, False, False, False, False, False, False))
# lg.append_line((True, True, True, False, False, False, False, False, False, False, False))
# lg.append_line((False, False, False, False, False, False, False, False, False, False, False))
# lg.append_line((False, False, False, False, False, False, False, False, False, False, False))
# lg.append_line((False, False, False, False, False, False, False, False, False, False, False))
# lg.append_line((False, False, False, False, False, False, False, False, False, False, False))
# lg.append_line((False, False, False, False, False, False, False, False, False, False, False))
# lg.append_line((False, False, False, False, False, False, False, False, False, False, False))
# lg.append_line((False, False, False, False, False, False, False, False, False, False, False))

# This is R-pentomino
# for i in range(23):
#     line = []
#     for j in range(40):
#         line.append(False)
#     lg.append_line(line)
#
# lline = []
# for i in range(23):
#     lline.append(False)
# lline.append(True)
# lline.append(True)
# for i in range(15):
#     lline.append(False)
# lg.append_line(lline)
#
# lline2 = []
# for i in range(22):
#     lline2.append(False)
# lline2.append(True)
# lline2.append(True)
# for i in range(16):
#     lline2.append(False)
# lg.append_line(lline2)
#
# lline3 = []
# for i in range(23):
#     lline3.append(False)
# lline3.append(True)
# for i in range(16):
#     lline3.append(False)
# lg.append_line(lline3)
#
# for i in range(14):
#     line = []
#     for j in range(40):
#         line.append(False)
#     lg.append_line(line)

# lg.zeros(15, 15)
# print(lg)
#
# print(len(lg.get_raw()))
#
# lg.ones(12, 12)
# print(lg)
#
# print(len(lg.get_raw()))

# R-pentamino
lg.zeros(40, 40)
lg.vitalize(23, 22)
lg.vitalize(23, 23)
lg.vitalize(24, 21)
lg.vitalize(24, 22)
lg.vitalize(25, 22)

print(lg)
print(len(lg.get_raw()))
print(len(lg.get_raw()[0]))

ax = plt.subplot(111)
canvas = ax.figure.canvas

def run(lg2):
    for _2 in lg2.run(70):
        plt.axis('off')
        plt.imshow(lg2.get_raw(), cmap=plt.cm.viridis) #, interpolation='quadric')
        canvas.draw()
        plt.clf()

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
