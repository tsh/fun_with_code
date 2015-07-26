import math

class Vector(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def length(self):
        """
        a.k.a magnitude
        """
        return math.sqrt(self.x*self.x + self.y*self.y)

    def mult(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)

    def div(self, scalar):
        return Vector(self.x/scalar, self.y/scalar)

    def normalized(self):
        """
        normalized vector is of length 1.
        Divide each component by vector length(magnitude)
        """
        return self.div(self.length())

class Point(object):
    def __init__(self, x=None, y=None):
        self.x=x
        self.y=y

    def add_vector(self, v):
        new_point = Point()
        new_point.x = self.x + v.x
        new_point.y = self.y + v.y
        return new_point

    def subtract(self, point):
        v = Vector()
        v.x = self.x - point.x
        v.y = self.y - point.y
        return v