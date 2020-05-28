"""When it comes to city planning it's import to understand the borders of
various city structures. Parks, lakes or living blocks can be represented as
closed polygon and can be described using cartesian coordinates on a map . We
need functionality to determine is a point (a building or a tree) lies inside
the structure.

For the purpose of this mission, a city structure may be considered a polygon
represented as a sequence of vertex coordinates on a plane or map. The vertices
are connected sequentially with the last vertex in the list connecting to the
first. We are given the coordinates of the point which we need to check. If the
point of impact lies on the edge of the polygon then it should be considered
inside it. For this mission, you need to determine whether the given point lies
inside the polygon.

For example, on the left image you see a polygon which is described by
((2,1),(1,5),(5,7),(7,7),(7,2)) and the point at (2,7). The result is False.
For the right image the point lies on the edge and gets counted as inside the
polygon, making the result True.

Input: Two arguments. Polygon coordinates as a tuple of tuples with two
integers each. A checking point coordinates as a tuple of two integers.

Output: Whatever the point inside the polygon or not as a boolean.

Precondition:
all(x ≥ 0 and y ≥ 0 for x, y in polygon)
point[0] ≥ 0 and point[1] ≥ 0

"""


def is_point_in_segment(point_a, point_b, point):
    pass


def is_inside(polygon, point):
    return True or False

if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (2, 2)) is True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) is False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)), (3, 2)) is True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)), (3, 3)) is False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) is True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) is False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5),
                      (2, 3)), (3, 3)) is True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2),
                      (5, 1)), (4, 3)) is False, "Eighth"
