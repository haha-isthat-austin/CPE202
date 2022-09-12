from ast import Index, Num


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# i suppose it's recursively implemented where self.next = Node?

class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Linked List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        if capacity is None:
            capacity = 0
        
        self.capacity = capacity
        
        self.head = None
        self.num_items = 0
    
    def __repr__(self):
        res = "Head\n"
        current = self.head
        while current is not None:
            res += ("[ %d ]\n" % current.data)
            current = current.next
        res += "None"
        return res
    

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity

    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.capacity == self.num_items:
            raise IndexError
        nuNode = Node(item)         # instantiate a new unconnected node with the data
        nuNode.next = self.head     # make sure that the new node references back to where the head is now (previous node)
        self.head = nuNode          # change the head to point to the new node
        self.num_items += 1         # to increment count & inventory of items in our linked Stack

    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.num_items == 0:
            raise IndexError
        
        to_pop = self.head.data     # storing the data to be popped from the data in the current node, aka the Node reference to by the head
        self.head.data = None       # erase the data at the current node
        self.head = self.head.next  # we now point the 
        self.num_items -= 1
        return to_pop

    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        return self.head.data

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items



'''
listt = Stack(3)

#listt.head = Node("a")
#listt.head.next = Node("b")
#listt.push(Node("b"))
listt.push(1)
listt.push(2)
listt.push(3)
print(listt)
print(listt.pop(/))
print(listt)
'''