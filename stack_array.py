# we are making a stack
# we are making a valid stack

from ast import Index
from multiprocessing.sharedctypes import Value


class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        if capacity is None:
            capacity = 0
        
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0 
    
    def __eq__(self, other):
        return (self.capacity, self.items, self.num_items) == (other.capacity, other.itmes, other.num_items)
    
    def __repr__(self):
        res = "Top of Stack\n"
        current = self.items[self.num_items]
        while self.num_items > 1:
            if current is None:
                res += ("[ None ]\n")
                self.num_items -= 1
            else:            
                res += ("[ %d ]\n" % current)
                self.num_items -= 1
        res += "None"
        return res

    # Stack implementation must be able to hold values of None as valid data
    # thought: "mt" but you also could still put in "mt" str or list (so comparisons don't work)
    # we also can't return errors per data input
    # 
    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        return self.capacity == self.num_items

    # self.is_full vs Stack.is_full
    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        self.items[self.num_items] = item
        self.num_items += 1

    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        self.num_items -= 1
        last_item = self.items[self.num_items]
        
        return last_item


    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        return self.items[self.num_items-1]

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items
'''
listt = Stack(3)
print(listt)
listt.push(None)
listt.push(None)
listt.push(None)

print(listt)
'''