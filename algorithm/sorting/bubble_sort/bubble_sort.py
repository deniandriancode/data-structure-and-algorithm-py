# -*- coding: utf-8 -*-
"""
Bubble sort is based on the idea of repeatedly comparing pairs of adjacent elements and then swapping their positions if they exist in the wrong order.
"""

def bubble_sort(arr):
    """Bubble sort implementation (ascending)

    Note: first iteration will put the largest element at the end of array,
    from there reduce the right end of array by one for each iteration.
    """
    l = 0
    r = len(arr)-1
    while l < r:
        for i in range(l, r):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        r -= 1

    return arr


arr = [8, 5, 7, 2, 4, 7, 0, 9]
print(arr)
arr = bubble_sort(arr)
print(arr)
