import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_basic_list(self):
        tlist = OrderedList()
        self.assertEqual(tlist.python_list(), [])
        self.assertEqual(tlist.python_list_reversed(), [])
        self.assertTrue(tlist.add(10))
        self.assertEqual(tlist.python_list(), [10])
        self.assertEqual(tlist.python_list_reversed(), [10])
        tlist.add(5)
        self.assertEqual(tlist.python_list(), [5, 10])
        #self.assertEqual(tlist.python_list_reversed(), [10, 5])
        tlist.add(-3)
        self.assertEqual(tlist.python_list(), [-3, 5, 10])
        tlist.add(100)
        self.assertEqual(tlist.python_list(), [-3, 5, 10, 100])
        self.assertEqual(tlist.python_list_reversed(), [100, 10, 5, -3])
        self.assertEqual(tlist.size(), 4)
        self.assertEqual(tlist.index(5), 1)
        self.assertTrue(tlist.search(100))
        self.assertTrue(tlist.search(-3))

    def test_invalid_indicies(self):
        tlist = OrderedList()
        with self.assertRaises(IndexError):
            tlist.pop(0)

        with self.assertRaises(IndexError):
            tlist.pop(-3)

        with self.assertRaises(IndexError):
            tlist.pop('three')

    def test_basic_list_reverse(self):
        tlist = OrderedList()
        self.assertTrue(tlist.add(5))
        tlist.add(3)
        self.assertEqual(tlist.python_list_reversed(), [5, 3])

    def test_string_list(self):
        # Testing making a string list
        tlist = OrderedList()
        self.assertTrue(tlist.add("apple"))
        self.assertTrue(tlist.add("banana"))
        self.assertTrue(tlist.add('strawberry'))
        self.assertFalse(tlist.add('apple'))
        self.assertEqual(tlist.python_list(), ['apple', 'banana', 'strawberry'])
        self.assertEqual(tlist.size(), 3)
        self.assertEqual(tlist.python_list_reversed(), ['strawberry', 'banana', 'apple'])
        self.assertTrue(tlist.remove('banana'))
        self.assertEqual(tlist.python_list(), ['apple', 'strawberry'])

    def test_invalid_comparisons(self):
        # Ensures a list containing integers does not have an add string operation
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertFalse(t_list.is_empty())
        with self.assertRaises(TypeError):
           t_list.add('hello')

    def test_simple_less_than_add(self):
        tlist = OrderedList()
        self.assertTrue(tlist.add(5))

        # Test adding to list item already exists
        self.assertFalse(tlist.add(5))

        self.assertTrue(tlist.add(3))

        # Test adding to list item already exists
        self.assertFalse(tlist.add(3))

        self.assertTrue(tlist.add(10))
        self.assertEqual(tlist.pop(2), 10)

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertTrue(t_list.remove(10))
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.add(10))
        self.assertEqual(t_list.pop(0), 10)

    def test_massive_list(self):
        tlist = OrderedList()
        compare_list = []
        for i in range(99, -1, -1):
            self.assertTrue(tlist.add(i))
        for i in range(100):
            compare_list.append(i)
        self.assertEqual(tlist.python_list(), compare_list)

        for i in range(99, -1, -1):
            self.assertTrue(tlist.search(i))
            self.assertEqual(tlist.pop(i), i)
            self.assertFalse(tlist.search(i))

    def test_remove(self):
        tlist = OrderedList()
        tlist.add('apple')
        tlist.add('banana')
        tlist.add('cucumber')
        tlist.add('dragon fruit')
        tlist.add('eggplant')
        self.assertEqual(tlist.python_list(), ['apple', 'banana', 'cucumber', 'dragon fruit', 'eggplant'])
        self.assertEqual(tlist.python_list_reversed(), ['eggplant', 'dragon fruit', 'cucumber', 'banana', 'apple'])
        self.assertTrue(tlist.remove('dragon fruit'))
        self.assertEqual(tlist.python_list(), ['apple', 'banana', 'cucumber', 'eggplant'])
        tlist.add('dragon fruit')
        self.assertEqual(tlist.python_list(), ['apple', 'banana', 'cucumber', 'dragon fruit', 'eggplant'])
        self.assertEqual(tlist.python_list_reversed(), ['eggplant', 'dragon fruit', 'cucumber', 'banana', 'apple'])

    def test_remove_single_list(self):
        tlist = OrderedList()
        tlist.add(10)
        self.assertEqual(tlist.size(), 1)
        self.assertTrue(tlist.remove(10))
        self.assertEqual(tlist.size(), 0)

    def test_remove_till_empty(self):
        tlist = OrderedList()
        tlist.add('apple')
        tlist.add('banana')
        tlist.add('cucumber')
        tlist.add('dragon fruit')
        tlist.add('eggplant')
        self.assertEqual(tlist.pop(3), 'dragon fruit')
        self.assertEqual(tlist.python_list(), ['apple', 'banana', 'cucumber', 'eggplant'])

        self.assertEqual(tlist.pop(2), 'cucumber')
        self.assertEqual(tlist.python_list(), ['apple', 'banana', 'eggplant'])

        self.assertTrue(tlist.remove('apple'))
        self.assertEqual(tlist.python_list(), ['banana', 'eggplant'])
        self.assertTrue(tlist.remove('eggplant'))
        self.assertEqual(tlist.size(), 1)
        self.assertTrue(tlist.search('banana'))
        self.assertEqual(tlist.python_list_reversed(), ['banana'])
        self.assertEqual(tlist.pop(0), 'banana')
        self.assertTrue(tlist.is_empty())
        self.assertEqual(tlist.size(), 0)
        self.assertEqual(tlist.python_list(), [])
        self.assertEqual(tlist.python_list_reversed(), [])

        pass


if __name__ == '__main__': 
    unittest.main()
