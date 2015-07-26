"""
Div and mult could be used for increasing or decreasing speed
"""
from structures import Vector, Point


if __name__ == '__main__':
    v = Vector(3, 4)
    print("Initial speed: ", v.length())

    vector_doubled = v.mult(2)
    print("Doubled speed: ", vector_doubled.length())

    vector_halved = v.div(2)
    print("Halved speed: ", vector_halved.length())
