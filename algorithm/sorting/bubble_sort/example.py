# Example program on using bubble sort

"""Problem

You have been given an array A of size N . you need to sort this array 
non-decreasing oder using bubble sort. However, you do not need to print 
the sorted array . You just need to print the number of swaps required 
to sort this array using bubble sort
"""

from typing import List # use list instead of array for simpler solution

def swap_count(arr: List) -> int:
    l = 0
    r = len(arr)-1
    c = 0 # swap counter
    while l < r:
        for i in range(r):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                c += 1

        r -= 1

    return c


arr = [1, 2, 3, 4, 6, 5]
print(swap_count(arr)) # should print 1

arr = [6, 5, 4]
print(swap_count(arr)) # should print 3
