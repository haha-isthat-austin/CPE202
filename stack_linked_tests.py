import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_linked import Stack
# from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    # my own tests
    def test_mystacktest(self):
        pass

if __name__ == '__main__': 
    unittest.main()

