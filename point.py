from math import exp, log
from functions.runge_kutta import runge_kutta


class Point:
    m = None
    x = None
    y = None

    def __init__(self, x, y, m=None):
        self.m = m
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'  # Это для вывода точки в консоль. Любая конвертация в строку

    def get_trajectory(self, t, dt):
        point_trajectory = [self]
        t_i = dt

        while t_i < t:
            point_trajectory.append(
                runge_kutta(point_trajectory[-1], t_i, dt)
            )
            t_i += dt

        point_trajectory.append(
            runge_kutta(point_trajectory[-1], t, dt)
        )

        return point_trajectory

    def copy(self):
        return Point(self.x, self.y, self.m)  # Из-за ссылочного хранения мы создаем новую точку с теми же параметрами.