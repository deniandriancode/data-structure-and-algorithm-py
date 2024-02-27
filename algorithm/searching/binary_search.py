# -*- coding: utf-8 -*-
"""Binary Search implementation

The following code is the implementation of binary
search algorithm for an array of integer.

Other types can be searched using the same implementation
logic
"""
from typing import List

def binary_search(arr: List[int], key: int, l: int, r: int) -> int:
    """Binary search implementation to search element `key` in array `arr`.

    Parameters
    ----------
    arr
        Array or List in which key to be searched. Array must be sorted.
    key
        Element to be searched.
    l
        Minimum index of array
    r
        Maximum index of array

    Returns
    -------
    int
        index of the first element if found, -1 if not found.
    """
    while l <= r:
        mid = int((l + r)/2)
        if key < arr[mid]:
            r = mid-1
        elif key > arr[mid]:
            l = mid+1
        else:
            return mid

    return -1

