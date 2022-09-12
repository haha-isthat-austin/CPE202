# from turtle import Turtle
# from queue_array import Queue
from queue_array import Queue
from multiprocessing.pool import IMapUnorderedIterator


class TreeNode:
    def __init__(self, key: int, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

def search_tree_help(node: TreeNode, key: int) -> bool:
    #print("node.key: ", node.key)
    if node is None:
        return False

    if node.key == key:
        return True

    if key > node.key:
        return search_tree_help(node.right, key)
    
    if key < node.key:
        return search_tree_help(node.left, key)

def insert_helper(node, nuNode):
    if node.key == nuNode.key:
        node.data = nuNode.data
    elif nuNode.key > node.key:
        if node.right is None:
            node.right = nuNode
        else:
            insert_helper(node.right, nuNode)
    elif nuNode.key < node.key:
        if node.left is None:
            node.left = nuNode
        else:
            insert_helper(node.left, nuNode)

def height_helper(node, height):
    if node.right is None and node.left is None:
        return height

    leftheight = 1
    rightheight = 1

    if node.right is not None:
        rightheight = height_helper(node.right, height + 1)

    if node.left is not None:
        leftheight = height_helper(node.left, height + 1)

    return max(rightheight, leftheight)

def inorder_helper(node, list_):
    if node.left is not None:
        inorder_helper(node.left, list_)
    
    list_.append(node.key)
    
    if node.right is not None:
        inorder_helper(node.right, list_)

def preorder_helper(node, list_):
    list_.append(node.key)

    if node.left is not None:
        preorder_helper(node.left, list_)
    
    if node.right is not None:
        preorder_helper(node.right, list_)

class BinarySearchTree:
    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root is None

    # iterative methodology requires dummy node
    # recursive mehtodology requires helper fnc

    def search(self, key): # returns True if key is in a node of the tree, else False
        return search_tree_help(self.root, key)

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        nuNode = TreeNode(key, data)

        if self.root is None:
            self.root = nuNode
        else:
            insert_helper(self.root, nuNode)

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        
        current = self.root
        while (current.left is not None):
            current = current.left
        return (current.key, current.data)

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        
        current = self.root
        while (current.right is not None):
            current = current.right
        return (current.key, current.data)        

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.root is None:
            return None

        return height_helper(self.root, 0)

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        listt = []
        inorder_helper(self.root, listt)
        return listt

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        listt = []
        preorder_helper(self.root, listt)
        return listt
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        listt = []

        if self.root is None:
            return listt

        q = Queue(25000) # Don't change this!

        q.enqueue(self.root)

        while (not q.is_empty()):
            node = q.dequeue()
            listt.append(node.key)

            if (node.left is not None):
                q.enqueue(node.left)

            if (node.right is not None):
                q.enqueue(node.right)

        return listt
        
'''
def test():
    tree = BinarySearchTree()

    tree.insert(100)
    tree.insert(200)
    tree.insert(150)
    tree.insert(5)
    tree.insert(1)
    tree.insert(50)
    tree.insert(75)
    tree.insert(60)

    # tree.print_tree()

    print(tree.search(60))
    print(tree.search(75))
    print(tree.search(76))

    print(tree.find_min())
    print(tree.find_max())

    print(tree.tree_height())

    tree2 = BinarySearchTree()
    tree2.insert(4)
    tree2.insert(2)
    tree2.insert(1)
    tree2.insert(3)
    tree2.insert(5)

    print(f"Inorder t2: {tree2.inorder_list()}")
    print(f"Inorder t1: {tree.inorder_list()}")

    print(f"Preorder t2: {tree2.preorder_list()}")
    print(f"Preorder t1: {tree.preorder_list()}")

    print(f"Level order t2: {tree2.level_order_list()}")
    print(f"Level order t1: {tree.level_order_list()}")

#if __name__ == "__main__":
#    test()

'''