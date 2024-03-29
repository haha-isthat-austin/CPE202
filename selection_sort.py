import random


def selectionSort(alist):
   count = 0
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax = 0
       for location in range(1,fillslot+1):
           count += 1
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location
       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
   return count


# Test cases:
# All cases are worst and best case. No matter what you, selection_sort has to iterate through
# the whole list and compare every single element with the rest of the elements.
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

n = 100
my_randoms = random.sample(range(10000), n)
count = selectionSort(my_randoms)
print(my_randoms)
print ("Random, n =", n, "comp comparison count =", count)

n = 200
my_randoms = random.sample(range(10000), n)
count = selectionSort(my_randoms)
print ("Random, n =", n, "comp comparison count =", count)

n = 100
reverse = list(range(n,0,-1))
count = selectionSort(reverse)
print(reverse)
print ("Reversed, n =", n, "comp comparison count =", count)

n = 200
reverse = list(range(n,0,-1))
count = selectionSort(reverse)
print ("Reversed, n =", n, "comp comparison count =", count)
