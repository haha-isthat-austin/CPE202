import unittest
from base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base_all_01(self):
        for i in range(2,17):
            for j in range(0,min(i,10)):
               self.assertEqual(convert(j,i),str(j))

    def digit_to_chr(digit: int) -> str:
        if digit < 10:
           return chr('0' + digit)

if __name__ == "__main__":
        unittest.main()