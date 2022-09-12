
from heapq import heapify
from turtle import right


class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.heaplist = [None]
        self.cur_size = len(self.heaplist) 

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        if self.is_full():
            return False
        self.heaplist += [item] # add item to the list
        self.cur_size += 1 # we increment before now                
        self.perc_up(self.cur_size)
        return True
        
    def perc_up(self, index_child):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        ''' Recursive '''
        parent_idx = self.get_parent(index_child)
        print(self.heaplist)

        if index_child <= 0 or parent_idx <= 0: # our base case
            return True

        if self.heaplist[parent_idx] < self.heaplist[index_child]:
            tmp = self.heaplist[parent_idx]
            self.heaplist[parent_idx] = self.heaplist[index_child]
            self.heaplist[index_child] = tmp
            self.perc_up(parent_idx)
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.heaplist[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        print(self.heaplist)
        if self.is_empty():
            return None
        our_max = self.heaplist[1]
        # Sets top to the last value in heap
        self.heaplist[1] = self.heaplist[-1]
        self.heaplist = self.heaplist[:len(self.heaplist) - 1]
        self.cur_size -= 1
        print("list: ", self.heaplist)
        print('size: ', self.cur_size)
        self.perc_down(1)
        return our_max
        

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.heaplist[1:]

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.heaplist[-1] == None

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.cur_size == self.capacity
        
    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.cur_size

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist'''
        if self.capacity < (len(alist) + 1):
            self.capacity = len(alist)

        self.heaplist = [None]
        self.cur_size = 0

        for i in alist:
            self.enqueue(i)


    def perc_down(self, parent_idx):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        left_child_idx = self.get_left_child(parent_idx)
        # Check to see if there is a left child
        # our cur_size is the # of items
        print(self.heaplist)
        print('left idx: ', left_child_idx)
        print('parent idx: ', parent_idx)
        if left_child_idx > (self.cur_size):
            # If not end function
            return

        if left_child_idx <= (self.cur_size):
            max_child_idx = self.max_child_idx(parent_idx)
            if self.heaplist[parent_idx] < self.heaplist[max_child_idx]:
                tmp = self.heaplist[parent_idx]
                self.heaplist[parent_idx] = self.heaplist[max_child_idx]
                self.heaplist[max_child_idx] = tmp
                self.perc_down(max_child_idx)

    def max_child_idx(self, parent_idx):
        right_child_idx = self.get_right_child(parent_idx)
        left_child_idx = self.get_left_child(parent_idx)
        if right_child_idx < self.cur_size:
            if self.heaplist[left_child_idx] < self.heaplist[right_child_idx]:
                return right_child_idx
        return left_child_idx

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''

        alist = alist.sort()

        '''
        self.build_heap(alist)
        self.heaplist = self.heaplist[1:]
        self.heaplist = self.heaplist.sort()
        print('self list: ', self.heaplist)
        alist = self.heaplist
        print('alist: ', alist)
        alist = alist[1:]
        alist = alist.sort()
        #print(alist)
        '''

    def get_left_child(self, index_parent):
        """Get index of left child"""
        return index_parent * 2

    def get_right_child(self, index_parent):
        return (index_parent * 2) + 1

    def get_parent(self, index_child):
        if index_child == 1:
            return index_child

        return (index_child) // 2
    
