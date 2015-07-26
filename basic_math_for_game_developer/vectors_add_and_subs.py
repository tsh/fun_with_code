"""
One can add two vector to go diagonal:
() ----------------> Horiz
 \ \
 \   \
 \     \
 \       \
 \         \
 \           \
 \|            \
 Vert         Diag

 If one need Diagonal vector, he could add Horiz + Vert.
"""
from structures import Vector, Point


if __name__ == '__main__':
    horizontal = Vector(4,0)
    vertical = Vector(0, -5)
    diagonal = horizontal.add(vertical)

    print("New velocity is: ", diagonal)
