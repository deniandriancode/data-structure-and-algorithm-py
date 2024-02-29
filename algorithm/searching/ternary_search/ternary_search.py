# -*- coding: utf-8 -*-
"""Ternary Search implementation

The following code is the implementation of ternary
search algorithm for an array of integer.

Other types can be searched using the same implementation
logic
"""
from typing import List

def ternary_search(arr: List[int], key: int, l: int, r: int) -> int:
    """Ternary search implementation to search element `key` in array `arr`.

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
        mid1 = int(l + (r - l)/3)
        mid2 = int(r - (r - l)/3)
        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2
        
        if key < arr[mid1]:
            r = mid1 - 1
        elif key > arr[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1

    return -1

