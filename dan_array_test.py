import unittest
from stack_array import *
#from stack_linked import *

class TestStackArray(unittest.TestCase):

    def test_everything(self):
        s = Stack(100)
        for i in range(100):
            s.push(None)
            self.assertEqual(None, s.peek())

    def test_is_full(self):
        stack = Stack(5)
        self.assertFalse(stack.is_full())
        stack.push(11)
        stack.push(12)
        stack.push(13)
        stack.push(14)
        stack.push(15)
        self.assertTrue(stack.is_full())
        stack.pop()


    def test_pop(self):
        stack = Stack(5)
        self.assertRaises(IndexError, stack.pop)
        self.assertEqual(stack.size(), 0) # Make sure trying to pop on empty stack didn't have an effect
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        stack.push(11)
        stack.push(12)
        stack.push(13)
        stack.push(14)
        stack.push(15)
        self.assertEqual(stack.pop(), 15)

    def test_peek(self):
        stack = Stack(5)
        self.assertRaises(IndexError, stack.peek)
        self.assertEqual(stack.size(), 0) # Make sure trying to peek on empty stack didn't have an effect
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        stack.push(11)
        self.assertEqual(stack.peek(), 11)

    def test_peek_size_BigO(self):
        size = 100000
        s = Stack(size)
        for i in range(size):
            self.assertEqual(i, s.size())
            s.push(i)
            self.assertEqual(i, s.peek())

    def test_push(self):
        stack = Stack(5)
        stack.push(11)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 11)


    def test_stack_one(self): # boundary case
        stack = Stack(1)
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),0)
        stack.push(11)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(),1)
        self.assertRaises(IndexError, stack.push, 12)
        self.assertEqual(stack.pop(),11)


    def test_stack_pushPopCombo_with_strings_and_floats_and_Nones(self):
        s = Stack(11)
        s.push('stuff')
        self.assertEqual(1, s.size())
        self.assertEqual('stuff', s.peek())


if __name__ == "__main__":
        unittest.main()