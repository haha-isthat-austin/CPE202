import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([0,0,0]), 0) # 
        self.assertEqual(max_list_iter([]), None) # makes sure None is raised
        #self.assertEqual(max_list_iter([-1, [], 2, 4]), 4)


    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([]),[])    # checking if my function can handle having nothing
        # self.assertEqual(reverse_rec([1,2,3]),[]) 
        self.assertEqual(reverse_rec([000]),[000])
        self.assertEqual(reverse_rec(["C","B","A"]),["A","B","C"]) # checking if it can handle strings well

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search1(self):
        list_val = [1, 2, 3, 4, 5, 6, 10, 11, 13, 1000, 10001]
        self.assertEqual(bin_search(4, 1, 7, list_val), 3)

    def test_bin_search2(self):
        list_val = [1, 2]
        self.assertEqual(bin_search(2, 0, 1, list_val), 1)        

    # making sure my fnc can handle just 2 inputs
    def test_bin_search3(self):
        list_val = [1, 2]
        self.assertEqual(bin_search(1, 0, 1, list_val), 0)    

    # making sure my fnc can jandle just 1 input 
    def test_bin_search4(self):
        list_val = [1]
        self.assertEqual(bin_search(1, 0, 1, list_val), 0)    

    # making sure my fnc can handle reversed high to low expectations
    def test_bin_search5(self):
        list_val = [1]
        self.assertEqual(bin_search(1, 0, 0, list_val), 0)   
        

if __name__ == "__main__":
        unittest.main()

    
