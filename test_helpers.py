import unittest
from exp_eval import *

class TestsInGeneral(unittest.TestCase):

    def test_Is_Float_(self):
       self.assertEqual(is_Float_('3.00'), True)

    def test_Is_Num_(self):
        self.assertEqual(is_Num_())

    def test_postfix(self):
        self.assertEqual(postfix_eval('3 4 +'), 7)

if __name__ == "__main__":
        unittest.main()