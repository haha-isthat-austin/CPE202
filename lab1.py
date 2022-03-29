
"""finds the max of a list of numbers and returns the value (not the index)  
If int_list is empty, returns None. If list is None, raises ValueError""" 

def max_list_iter(int_list):  # must use iteration not recursion
    x = 0 

    if len(int_list) == 0:
        return None
    else:
        for i in int_list:
            if i > x:
                x = i
            else:
                pass
        return x

list_2 = [1, 2, 3]
#print(max_list_iter(list_2))

poplist = [] # our pop-out list 
endlist = [] # final list


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if len(int_list) == 0:              # this will work once and once only
        endlist.append(poplist[0])
    else:
        poplist.append(int_list[0])

pritn(reverse_rec(list_2))

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
