import unittest
from area import area
from math import pi
from area import subtraction

class TestAreaFunction(unittest.TestCase):
    def test_radius_type(self):
        self.assertRaises(TypeError,area, 2+5j)

    def test_subtraction(self):
        self.assertEquals(subtraction(15,5), 10)


    def test_area_function(self):
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2.2),pi* 2.2 **2)

    def test_area_value(self):
        self.assertRaises(ValueError,area, -1)
