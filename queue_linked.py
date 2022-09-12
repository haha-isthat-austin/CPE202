
class Node:
    def __init__(self,item):
        self.data = item
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        if type(capacity) != int:
            raise ValueError
        self.capacity = abs(capacity)
        self.num_items = 0
        self.head = None
        self.front = None


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        # for the first item, we have self.head_of to always call back in O(1) manner
        nuNode = Node(item)
        if self.is_empty():  # list is empty
            self.front = nuNode
            self.head = nuNode
            self.num_items += 1
        else: # list isn't empty
            self.head.next = nuNode
            self.head = nuNode
            self.num_items += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError     
        res = self.front.data
        self.front = self.front.next
        self.num_items -= 1

        return res


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
'''
q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.size())
print(q.dequeue() == 1)
'''

'''
test0 = Queue(2)
test0.enqueue('wtf')
#print(test0.head.next)
#print(test0.front.next)
test0.enqueue('wtf2')
print(test0.head.data)
print(test0.front.data)
test = Queue(5)
#print(test.is_full())
#test.enqueue(1)
#print(test.front.data)
#print(test.head.data)
#print(test.head.next)
#test2 = Queue(0)
#print(test2.is_empty())
#test.enqueue(2)
#test.enqueue(3)
#print(test.dequeue())
#print(test.dequeue())
#print(test.dequeue())
#print(test.dequeue())

#test.dequeue()
#test.dequeue()
#print(test.is_empty())
#print(test.head.data)
#print(test.front.data)
'''