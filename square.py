from math import pi, cos, sin, sqrt
from classes.point import Point


class Square:
    length = None
    point_cnt = None
    points = []
    center = None
    angle = None

    def __init__(self, length, center, point_cnt=10, angle=pi/4):
        self.length = length
        self.center = center
        self.point_cnt = point_cnt
        self.angle = angle
        self.points = self.get_points()

    def get_points(self):
        points = []
        point_i = Point(
            self.center.x + self.length * sqrt(2) * cos(self.angle) / 2,
            self.center.y + self.length * sqrt(2) * sin(self.angle) / 2
        )
        h = 4 * self.length / self.point_cnt
        for i in range(self.point_cnt // 4):
            points.append(point_i.copy())
            point_i.x += h * cos(pi - pi/4 - self.angle)
            point_i.y -= h * sin(pi - pi/4 - self.angle)

        for i in range(self.point_cnt // 4):
            points.append(point_i.copy())
            point_i.x -= h * cos(-pi / 4 + self.angle)
            point_i.y -= h * sin(-pi / 4 + self.angle)

        for i in range(self.point_cnt // 4):
            points.append(point_i.copy())
            point_i.x -= h * cos(pi - pi / 4 - self.angle)
            point_i.y += h * sin(pi - pi / 4 - self.angle)

        for i in range(self.point_cnt // 4):
            points.append(point_i.copy())
            point_i.x += h * cos(-pi / 4 - self.angle)
            point_i.x += h * sin(-pi / 4 + self.angle)

        points.append(Point(
            self.center.x + self.length * sqrt(2) * cos(self.angle) / 2,
            self.center.y + self.length * sqrt(2) * sin(self.angle) / 2
        ))
        return points