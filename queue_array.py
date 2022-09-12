
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        if type(capacity) != int:
            raise ValueError
        self.capacity = abs(capacity)
        self.items = [None]*capacity
        self.head = 0
        self.tail = 0
        self.num_items = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == 0:
            return True
        return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:
            return True
        return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        self.items[self.tail] = item
        self.tail += 1
        self.num_items += 1

        if self.tail >= self.capacity:
            self.tail = 0


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        # how do i move everything over when I delete ?
        # move the end num. of items down 1 and then return 
        if self.is_empty():
            raise IndexError
        res = self.items[self.head]
        self.head += 1
        self.num_items -= 1

        if self.head >= self.capacity:
            self.head = 0        

        return res

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
'''
test = Queue(6)
#print(test.capacity)
#print(test.is_empty())
#print(test.is_full())
test.enqueue(1)
#print(test.items[test.head])
#print(test.tail)
test.enqueue(-2)
test.enqueue(3.00)
test.enqueue(4)
#print(test.items[test.head])
#print(test.dequeue())
#print(test.items[test.head])
'''

#test2 = Queue(-1)
#print(test2.capacity)
#test3 = Queue(3.3333)
#test3 = Queue(0)
#print(test3.is_empty())
#print(test3.capacity)
#test3.dequeue()
#test4 = Queue(1)
#test4.enqueue(10000)
#print(test4.is_empty())
#print(test4.is_full())
