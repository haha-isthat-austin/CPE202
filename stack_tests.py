import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
#from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    # my own tests
    def test_mystacktest(self):
        stack = Stack(10)
        stack.push(None)
        #print(stack)
        #print(stack.num_items)
        #print(stack.is_empty())
        self.assertFalse(stack.is_empty())

    def test_empty_list(self):
        stack = Stack(None)
        '''
        print(stack.capacity)
        print(stack.num_items)
        print(stack.is_empty())
        '''
        self.assertTrue(stack.is_empty())

if __name__ == '__main__': 
    unittest.main()

