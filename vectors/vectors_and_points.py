"""
Add vector to a point
"""

class Vector(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


class Point(object):
    def __init__(self, x=None, y=None):
        self.x=x
        self.y=y

    def add_vector(self, v):
        new_point = Point()
        new_point.x = self.x + v.x
        new_point.y = self.y + v.y
        return new_point

if __name__ == '__main__':
    point = Point(1,0)
    vector = Vector(2,3)
    point2 = point.add_vector(vector)
    print(point2.x, point2.y)
