import unittest
#from queue_array import Queue
from queue_array import Queue
#from queue_array2 import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue_fill_to_capacity_and_dequeue_all(self):
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 0)
        self.assertRaises(IndexError, q.dequeue)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertRaises(IndexError,q.enqueue,6)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)

    def test_everything_and_big_O(self):
        size = 50000
        q = Queue(size)
        for i in range(size):
            q.enqueue(i)
        for i in range(size):
            self.assertEqual(q.dequeue(), i)
            q.enqueue(i)

if __name__ == '__main__': 
    unittest.main()
