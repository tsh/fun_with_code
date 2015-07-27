"""
Dot product could be use to determine, is 2 object watch in a same or different director
1  -> same direction
0  -> 90 degree
-1 -> opposite direction
"""
from structures import Vector, Point

if __name__ == '__main__':
    blu_player_view_vector = Vector(3, 0)
    red_player_view_vector = Vector(-6, 0)
    print("Dot product of the vectors is: ", blu_player_view_vector.dot_product(red_player_view_vector))
