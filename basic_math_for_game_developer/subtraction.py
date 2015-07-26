"""
Substraction is used to figure out vector from one point to another
V = P(destination) - P(current)
"""

from structures import Vector, Point

if __name__ == '__main__':
    destination = Point(0, -1)
    current_position = Point(1, 1)

    v = destination.subtract(current_position)
    print(v.x, v.y)
