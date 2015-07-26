"""
Normalized vector is vector of length 1. Used where one direction is matter.
E.g: direction of the view, direction of movement, etc.
"""
from structures import Vector, Point


if __name__ == '__main__':
    p= Point(3,4)
    i = Point(1,2)
    pi = p.subtract(i)
    normalized_vector = pi.normalized()

    print("view vector: ", normalized_vector.x, normalized_vector.y)
    print("view vector length: ", normalized_vector.length())