from pyparsing import Or


class Node:
    '''Node for use with doubly-linked list'''

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = Node(None)

    def __eq__(self, other):
        return self.item == other.item

    def __lt__(self, other):
        return self.item < other.item

    def __gt__(self, other):
        return self.item > other.item

    def __repr__(self):
        s = ""
        tmp = self.head.next
        while (tmp is not self.head):
            s = s + f"{tmp.item}, "
            tmp = tmp.next
        return s

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.head.next is self.head or self.head.next is None

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        nuNode = Node(item)
        # if the list is empty:
        if self.head.next is None:

            self.head.prev = nuNode
            self.head.next = nuNode

            nuNode.prev = self.head
            nuNode.next = self.head
            return True
        # otherwise, if the list is not empty, sort it
        else:
            prev_node = self.head.prev
            # checking to see if our item is the smallest (we reach the end) or if it's bigger than any singular value
            while prev_node is not self.head and prev_node.item > nuNode.item:
                prev_node = prev_node.prev
            # in case the item is already in the list
            if prev_node.item is nuNode.item:
                return False

            # make our new node's prev point to the current node
            nuNode.prev = prev_node
            # make our new node's next point to the current node's next
            nuNode.next = prev_node.next
            # current node's next is now the new node
            prev_node.next = nuNode
            # the next of the new node is now the next node of the old current node
            prev_node = nuNode.next
            # the old current node's next now has to refer back to the new node
            prev_node.prev = nuNode
            return True

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list)
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        if self.is_empty():
            return False

        prev = self.head.prev
        while prev is not self.head and prev.item is not item:
            prev = prev.prev

        # if the item still isn't found by the last item
        if prev.item is not item:
            return False
        else:
            # the current node, prev, is therefore the node of excision
            # the previous node's next pointer will now be the current node's next
            # prev.item = None
            cur_node_next = prev.next  # to-be-executed node's next
            cur_node_prev = prev.prev  # to-be-executed node's previous
            cur_node_prev.next = cur_node_next
            cur_node_next.prev = cur_node_prev

            return True

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''

        if self.is_empty():
            return None

        tmp = self.head.next
        idx = 0
        while tmp is not self.head and tmp.item is not item:
            idx += 1
            tmp = tmp.next
        if tmp.item != item:
            return None
        else:
            return idx

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''

        if index < 0 or index >= self.size():
            raise IndexError

        idx_count = 0
        tmp_pop = self.head.next
        while tmp_pop is not self.head and idx_count is not index:
            idx_count += 1
            tmp_pop = tmp_pop.next

        res = tmp_pop.item
        self.remove(res)
        return res

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        if self.is_empty():
            return False

        return self.search_help(self.head.next, item)

    def search_help(self, node, item):
        # print("Node.item: ", node.item)

        if node.item is item:
            return True
        elif node.next is self.head and node.item is not item:
            return False

        return self.search_help(node.next, item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        res = []

        if self.is_empty():
            return res

        tmp = self.head.next
        while tmp is not self.head:
            res.append(tmp.item)
            tmp = tmp.next
        return res

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        rev = self.head.prev
        res = []
        while rev is not self.head:
            res.append(rev.item)
            rev = rev.prev

        return res

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        if self.head.next is self.head or self.head.next is None:
            return 0
        return self.size_help(self.head.next)

    def size_help(self, node):
        if node is self.head:
            return 0
        return 1 + self.size_help(node.next)


# list1 = OrderedList()
# print(list1 == [])

'''
t_list = OrderedList()
t_list.add(10)
t_list.add(30)
t_list.add(5)
t_list.add(15)
t_list.add(20)
t_list.add(35)
t_list.add(25) # add a bunch of numbers 
print(t_list.python_list())
print(t_list.is_empty())
#t_list.python_list(), [5, 10, 15, 20, 25, 30, 35] # make sure they are ordered
t_list.remove(10)
t_list.remove(20) # remove some items in the middle
#t_list.python_list(), [5, 15, 25, 30, 35] # check to see if the list still matches
print(t_list.python_list())
print(t_list.is_empty())
print("false 17: ", t_list.remove(17)) # get a false return if you try to remove an item not in the list
print(t_list.python_list())
t_list.remove(5)
t_list.remove(15)
t_list.remove(25) # remove a bunch of items from the list
t_list.remove(30)
t_list.remove(35)
print(t_list.head is t_list.head.next)
print(t_list.head)
print(t_list.head.next)
print(t_list.head.prev)
print(t_list.python_list())
print(t_list.is_empty())

#test5 = OrderedList()
#print(test5.is_empty())
'''
'''
test1 = OrderedList()
test1.add(1)
test1.add(2)
test1.add(3)
test1.add(-2)
test1.add(1888)
test1.add(7.7)
#print('test1: ', test1)
#print('test1 size: ', test1.size())
#print(test1.search(5))
'''
'''
print(test1.index(2))
print(test1.search(2))
print(test1.search(1))
print(test1.search(3))
print(test1.search(4))
print(test1.search(-1))
'''
# print(test1.size())
# print(test1.pop(0))

# print("Py list: ", test1.python_list())
# print("Py list rev: ", test1.python_list_reversed())

'''
test0 = OrderedList()
#print(test0)
test0.add(1)
test0.add(2)
test0.add(3)
test0.add(4)
print(test0)
print("size: ", test0.size())
print(test0.remove(1))
print("After we remove 1: " , test0)
test0.add(1)
test0.remove(4)
print("After we remove 4: ", test0)
test0.add(4)
test0.remove(2)
print("After we remove 2: ", test0)
print(test0.size())
'''
'''
test0.add(3) # test if it adds a redundant value
test0.add(4)
print(test0)
print(test0.index(4))
'''