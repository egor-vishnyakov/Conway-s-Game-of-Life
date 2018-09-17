import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as manimation
from matplotlib.animation import ImageMagickFileWriter


def life(X, steps):
    """
     Conway's Game of Life.
     - X, matrix with the initial state of the game.
     - steps, number of generations.
    """
    def roll_it(x, y):
        # rolls the matrix X in a given direction
        # x=1, y=0 on the left;  x=-1, y=0 right;
        # x=0, y=1 top; x=0, y=-1 down; x=1, y=1 top left; ...
        return np.roll(np.roll(X, y, axis=0), x, axis=1)

    for _ in range(steps):
        # count the number of neighbours
        # the universe is considered toroidal
        Y = roll_it(1, 0) + roll_it(0, 1) + roll_it(-1, 0) \
            + roll_it(0, -1) + roll_it(1, 1) + roll_it(-1, -1) \
            + roll_it(1, -1) + roll_it(-1, 1)
        # game of life rules
        X = np.logical_or(np.logical_and(X, Y ==2), Y==3)
        X = X.astype(int)
        yield X


X = np.zeros((40, 40)) # 40 by 40 dead cells

# R-pentomino
X[23, 22:24] = 1
X[24, 21:23] = 1
X[25, 22] = 1

ax = plt.subplot(111)
canvas = ax.figure.canvas

def run(lg2):
        for x in life(lg2, 170):
            plt.axis('off')
            plt.imshow(x, cmap=plt.cm.viridis) #, interpolation='quadric')
            canvas.draw()
            plt.clf()

manager = plt.get_current_fig_manager()
manager.window.after(100, run, X)
plt.show()

# FFMpegWriter = manimation.writers['avconv']
# metadata = dict(title='Game of life', artist='JustGlowing')
# writer = ImageMagickFileWriter(fps=10, metadata=metadata)
#
# fig = plt.figure()
# fig.patch.set_facecolor('black')
# with writer.saving(fig, "game_of_life.mp4", 200):
#     plt.spy(X)
#     plt.axis('off')
#     writer.grab_frame()
#     plt.clf()
#     for x in life(X, 50):
#         plt.spy(x)
#         plt.axis('off')
#         writer.grab_frame()
#         plt.clf()
