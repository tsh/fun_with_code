"""
Length of the vector -> distance between 2 point or another words: how far we have to go?)
"""
from structures import Vector, Point

if __name__ == '__main__':
    destination = Point(0, -1)
    current_position = Point(1, 1)

    v = destination.subtract(current_position)
    print("Length between destination and current position is", v.length())
