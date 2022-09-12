"""finds the max of a list of numbers and returns the value (not the index)
If int_list is empty, returns None. If list is None, raises ValueError"""


def max_list_iter(int_list: list[int]):  # must use iteration not recursion
    x = 0

    if int_list is None:
        raise ValueError

    if not int_list:
        return None

    _max = int_list[0]
    for i in int_list:
        if i > _max:
            _max = i

    return _max


# list_2 = [1, 2, 3]


# print(max_list_iter(list_2))
# print(len(list_2))

def reverse_rec(int_list: list[int]):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError

    if len(int_list) == 0:
        return []

    #    print("last term of list", int_list[-1])
    #   print("what is recursed into the fnc", reverse_rec(int_list[:-1]))
    return [int_list[-1]] + reverse_rec(int_list[:-1])


# print(reverse_rec(list_2))


def bin_search(target: int, low: int, high: int, int_list: list[int]):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    # print(int_list)

    if int_list is None:
        raise ValueError

    if low > high:
        return None

    mid = (low + high) // 2

    if target < int_list[mid]:
        return bin_search(target, low, mid - 1, int_list)
    elif target > int_list[mid]:
        return bin_search(target, mid + 1, high, int_list)
    else:
        return mid




# print(bin_search(2, 1, 5, [0, 1, 2, 3, 4, 5, 6]))

# print(list_2[:(1+1])  this proves that we indeed can go

# How do we keep a track on indices, I know that the current method of slicing recursively allows us
