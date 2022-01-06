from polygon import *
from polygon_seq import *

def test_polygon():
    p1 = RegConvexPolygon(10, 4)
    p2 = RegConvexPolygon(10, 4)
    p3 = RegConvexPolygon(100, 2)
    p4 = RegConvexPolygon(2, 100)
    p5 = RegConvexPolygon(10, 2)

    assert p1 == p2
    assert p1 != p5
    assert p3 > p4
    assert p3 > p2
