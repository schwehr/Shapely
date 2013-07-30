import unittest
from shapely.geometry import MultiPolygon
from shapely.geometry import Point
from shapely.ops import cascaded_union

class CascadedUnionTestCase(unittest.TestCase):
    def test_1(self):
        polygons = [Point(i, 0).buffer(0.7) for i in range(5)]
        self.failUnlessAlmostEqual(cascaded_union(polygons).area, 6.610301355116797)
        m = MultiPolygon(polygons)
        self.failUnlessAlmostEqual(m.area, 7.684543801837549)
        self.failUnlessAlmostEqual(cascaded_union(m).area, 6.610301355116797)
        self.failUnlessAlmostEqual(cascaded_union([m, m]).area, 6.610301355116797)

def test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(CascadedUnionTestCase)
