
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
#print(len(list_2))

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if len(int_list) == 0:
        return []

#    print("last term of list", int_list[-1])
 #   print("what is recursed into the fnc", reverse_rec(int_list[:-1]))
    return [int_list[-1]] + reverse_rec(int_list[:-1])



#print(reverse_rec(list_2))

def Tyler_rec(int_list):   
    if len(int_list) == 0:
        return []

    return int_list.append(reverse_rec(int_list[:-1]))

# print(Tyler_rec(list_2))

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list[0] == target:
        return [1]               # this base case changes...
    else: 
        return None

    return len(int_list) -  sum[bin_search(target, low, high, int_list[:-1])]


# How do we keep a track on indices, I know that the current method of slicing recursively allows us 

