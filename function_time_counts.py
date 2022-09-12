import random
import time

def insertion_sort(alist):
    count = 0
    for i in range(1, len(alist)):
        temp = alist[i]

        j = i - 1
        if temp < alist[j]:
            while temp < alist[j] and j >= 0:
                alist[j+1] = alist[j]
                j -= 1
                count +=1
            alist[j+1] = temp
        else:
            count += 1
    return count

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

def insertion_sort_time_avg():
    print("Insertion sort run times:\n")
    number_of_average = 5
    for exponent in range(6):

        n = pow(2,exponent) * 1000
        total_time = 0
        total_sort_count = 0
        for i in range(number_of_average):

            input_list = random.sample(range(100000), n)
            tic = time.perf_counter()
            sort_count = insertion_sort(input_list)
            toc = time.perf_counter()

            total_sort_count += sort_count
            total_time += (toc - tic)

        print("==============================\n")
        print("Length of input list:", n)
        print("Average number of comparisons:", total_sort_count//number_of_average)
        print("Time taken of", number_of_average, "averages = %3.5f seconds\n" %(total_time/number_of_average))
        print("==============================\n")

def selection_sort_time_avg():
    print("Selection sort run times:\n")
    number_of_average = 5
    for exponent in range(6):

        n = pow(2,exponent) * 1000
        total_time = 0
        total_sort_count = 0
        for i in range(number_of_average):

            input_list = random.sample(range(100000), n)
            tic = time.perf_counter()
            sort_count = selectionSort(input_list)
            toc = time.perf_counter()

            total_sort_count += sort_count
            total_time += (toc - tic)

        print("==============================\n")
        print("Length of input list:", n)
        print("Average number of comparisons:", total_sort_count//number_of_average)
        print("Time taken of", number_of_average, "averages = %3.5f seconds\n" %(total_time/number_of_average))
        print("==============================\n")

#insertion_sort_time_avg()
#selection_sort_time_avg()


PIVOT_FIRST = 0
PIVOT_MIDDLE = 1
PIVOT_MEDIAN_3 = 3

pivot_method = PIVOT_FIRST


print("Pivot method: ", pivot_method)
total_count = 0

def quick_sort(alist):
   global total_count
   total_count = 0
   quick_sort_helper(alist,0,len(alist)-1)

def quick_sort_helper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)
       quick_sort_helper(alist,first,splitpoint-1)
       quick_sort_helper(alist,splitpoint+1,last)

def partition(alist,first,last):
   global total_count
   mid = (first+last)//2
   if pivot_method == PIVOT_FIRST:
      piv_index = first
   elif pivot_method == PIVOT_MIDDLE:
      piv_index = mid
   else:
      median_list = [alist[first], alist[mid], alist[last]]
      median_list.sort()
#      print("med:", median_list, median_list[1])
      if alist[first] == median_list[1]:
          piv_index = first
      elif alist[mid] == median_list[1]:
          piv_index = mid
      else:
          piv_index = last

#   piv_index = (first+last)//2
   pivotvalue = alist[piv_index]
   temp = alist[first] # move pivot out of the way
   alist[first] = alist[piv_index]
   alist[piv_index] = temp
#   print("list start:", alist)
#   print("pivot:", pivotvalue)

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           total_count += 1
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           total_count += 1
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]          # put pivot into splitpoint
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

#   print("list done :", alist) print()

   return rightmark


def QuickSort_time_avg():
    print("Quicksort run times:\n")
    number_of_average = 10
    for exponent in range(4):

        n = pow(2,exponent) * 100
        total_time = 0
        total_sort_count = 0
        for i in range(number_of_average):
            input_list = list(range(n))
            #input_list = random.sample(range(10000), n)
            tic = time.perf_counter()
            quick_sort(input_list)
            toc = time.perf_counter()

            total_time += (toc - tic)
            total_sort_count += total_count

        print("==============================\n")
        print("Length of input list:", n)
        print("Average number of comparisons:", total_sort_count//number_of_average)
        print("Time taken of", number_of_average, "averages = %3.5f seconds\n" %(total_time/number_of_average))
        print("==============================\n")

QuickSort_time_avg()