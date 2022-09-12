import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_wowow(self):
        t_list = OrderedList() 
        self.assertTrue(t_list.is_empty())

    def test_02a_add(self):
        t_list = OrderedList()
        self.assertTrue(t_list.add(10))

    def test_02a_add_HuffmanNodes(self):
        t_list = OrderedList()
        self.assertTrue(t_list.add(HuffmanNode('a', 10)))

    def test_03_remove(self):
        t_list = OrderedList()
        self.assertFalse(t_list.remove(5))

    def test_03a_remove_HuffmanNodes(self):
        t_list = OrderedList()
        self.assertFalse(t_list.remove(5))

    def test_04_index(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertEqual(t_list.index(10), 0)

    def test_04a_index_HuffmanNodes(self):
        t_list = OrderedList()
        t_list.add(HuffmanNode('a', 10))
        t_list.add(HuffmanNode('b', 10))
        t_list.add(HuffmanNode('e', 15))
        t_list.add(HuffmanNode('f', 15))
        t_list.add(HuffmanNode('c', 30))
        self.assertEqual(t_list.index(HuffmanNode('a', 10)), 0)

    def test_05_pop(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertRaises(IndexError, t_list.pop, -1)
        self.assertEqual(t_list.size(), 5)
        self.assertRaises(IndexError, t_list.pop, 5)
        self.assertEqual(t_list.size(), 5)
        self.assertEqual(t_list.pop(0), 10)
        self.assertEqual(t_list.python_list(), [20, 30, 40, 50])
        self.assertEqual(t_list.python_list_reversed(), [50, 40, 30, 20])
        self.assertEqual(t_list.size(), 4)
        self.assertEqual(t_list.pop(3), 50)
        self.assertEqual(t_list.python_list(), [20, 30, 40])
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.pop(1), 30)
        self.assertEqual(t_list.python_list(), [20, 40])
        self.assertEqual(t_list.size(), 2)
        self.assertEqual(t_list.pop(0), 20)
        self.assertEqual(t_list.python_list(), [40])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.pop(0), 40)
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())

    def test_06_search(self):
        t_list = OrderedList()
        self.assertFalse(t_list.search(10))

    def test_07_python_list(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(),[])

    def test_08_size_is_empty(self):
        t_list = OrderedList()
        self.assertEqual(t_list.size(),0)

    def test_09_add_remove_all_add(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(200):
            self.assertTrue(t_list.remove(val))
        self.assertTrue(t_list.is_empty())

    def test_10_add_pop_all_add(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(199, -1, -1):
            self.assertEqual(t_list.pop(val), val)
        self.assertTrue(t_list.is_empty())

    def test_11_add_pop_remove(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(100):
            self.assertEqual(t_list.pop(0), val)
            self.assertTrue(t_list.remove(199-val))
        print(t_list)
        self.assertTrue(t_list.is_empty())
'''
    def test_14_python_list_reversed_is_recursive01(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150) 
        #with self.assertRaises(RecursionError)

    def test_17_python_list_reversed_is_recursive02(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150)
        with self.assertRaises(RecursionError):

    def test_19_python_list_reversed_is_recursive03(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150)
        with self.assertRaises(RecursionError):
'''

'''
    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
'''

if __name__ == '__main__': 
    unittest.main()
