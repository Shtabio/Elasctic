import matplotlib.pyplot as plt


def plot_trajectory(square, t, dt):
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    for point in square.points:
        trajectory = point.get_trajectory(t, dt)
        plt.plot(list(map(lambda p: p.x, trajectory)), list(map(lambda p: p.y, trajectory)))
    plt.show()