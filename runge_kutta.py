from math import exp, log
import numpy as np

import matplotlib.pyplot as plt


def velocity_x(t, x):
    return -exp(t) * x


def velocity_y(t, y):
    return log(t) * y


def runge_kutta(p, t, dt):
    k1_x = velocity_x(t, p.x)
    k2_x = velocity_x(t + dt * 1 / 3, p.x + dt * k1_x / 3)
    k3_x = velocity_x(t + dt * 2 / 3, p.x + 2 * dt * k2_x / 3)
    p.x += dt * (0.25 * k1_x + 0.75 * k3_x)

    k1_y = velocity_y(t, p.y)
    k2_y = velocity_y(t + dt * 1 / 3, p.y + dt * k1_y / 3)
    k3_y = velocity_y(t + dt * 2 / 3, p.y + 2 * dt * k2_y / 3)
    p.y += dt * (0.25 * k1_y + 0.75 * k3_y)

    return p.copy()  # В питоне ссылочное хранение. Если возвращать р, то передастся ссылка, а мы меняем р.
                    # То есть каждый раз мы даем ссылку на один и тот же объект памяти, который меняем.
                    # Итого массив одинаковых точек, что нам не надо.
                    # Поэтому мы каждый раз копируем точку в новую ячейку памяти.
                    # И потом собирается массив этих точек в методе class Point