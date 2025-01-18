import matplotlib.pyplot as plt
import numpy as np
from classes.square import Square
from classes.point import Point
from functions.plot_streamlines import plot_streamlines
from functions.plot_trajectory import plot_trajectory


a = Square(1, Point(-1.5, -1.5))
plt.plot(list(map(lambda p: p.x, a.points)), list(map(lambda p: p.y, a.points)))
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()


plot_trajectory(a, 1, 0.1)

for t in np.arange(0.1, 1, 0.1):
    plot_streamlines(t, -10,10)
