import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1, Location("SLO", 35.3, -120.7))
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1, loc2)
    # Add more tests!

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        str1 = "Location('SLO', 35.3, -120.7)"
        str2 = "Location(SLO, 35.3, -120.7)"
        res = repr(loc)
        print(res)
        print(res == str1)
        print(res == str2)
        self.assertTrue(res == str1 or res == str2)

if __name__ == "__main__":
        unittest.main()
