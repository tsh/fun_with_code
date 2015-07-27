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

    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def subtract(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)

    def normalized(self):
        """
        normalized vector is of length 1.
        Divide each component by vector length(magnitude)
        """
        return self.div(self.length())

    def dot_product(self, vector):
        """
        For our purposes as view vector, dot product is calculated on a normal vectors.
        Hence we will use explicit normalization
        """
        normal_self = self.normalized()
        normal_vector = vector.normalized()
        return normal_self.x*normal_vector.x + normal_self.y*normal_vector.y

    def __str__(self):
        return "Vector<{x}, {y}>".format(x=self.x, y=self.y)

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