from classes.stream_lines import StreamLine
import matplotlib.pyplot as plt
import numpy as np


def plot_streamlines(t, min_val, max_val, skip=20):  #skip нужен, чтобы прореживать точки для отрисовки графика
    # создаем массивы для покрытия поля координатной сеткой, чтобы потом нарисовать линии тока и скорость
    x_vals = np.linspace(min_val, -1, abs(min_val) * 10 + 1)
    y_vals = np.linspace(1, max_val, max_val * 10 + 1)
    x, y = np.meshgrid(x_vals, y_vals)

    s = StreamLine(t, x, y)  #здесь мы передаем в StreamLine np массивы х и у. np умный.
                            # По-хорошему надо передавать числа.
                            # Но np подставляет сам каждый элемент массива и дает обратно массив.
                            # Чтобы вы ручками это не делали.

    # прореживание поля для отрисовки
    x_tangent = x[::skip, ::skip]
    y_tangent = y[::skip, ::skip]
    v1 = s.vx[::skip, ::skip]
    v2 = s.vy[::skip, ::skip]

    plt.figure(figsize=(10, 6))
    plt.streamplot(x, y, s.vx, s.vy, density=1, color='red')
    plt.quiver(x_tangent, y_tangent, v1, v2, scale=100)
    plt.title(f'time = {round(t, 2)}')
    plt.xlim(min_val, 0)
    plt.ylim(0, max_val)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()