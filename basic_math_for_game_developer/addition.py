"""
Addition used to move move point in direction of the vector
"""
from structures import Vector, Point

if __name__ == '__main__':
    point = Point(1,0)
    vector = Vector(2,3)
    point2 = point.add_vector(vector)
    print(point2.x, point2.y)
