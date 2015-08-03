import math


class Vector(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def add(self, v):
        self.x += v.x
        self.y += v.y

    def sub(self, v):
        self.x -= v.x
        self.y -= v.y

    @classmethod
    def static_sub(cls, v1, v2):
        return Vector(v1.x-v2.x, v1.y-v2.y)

    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def div(self, scalar):
        self.x /= scalar
        self.y /= scalar

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude != 0:
            self.div(math.ceil(magnitude))


