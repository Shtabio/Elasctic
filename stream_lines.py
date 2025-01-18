from math import log, exp


class StreamLine:
    vx = None
    vy = None

    def __init__(self, t, x, y):
        self.vx = -exp(t) * x
        self.vy = log(t) * y
