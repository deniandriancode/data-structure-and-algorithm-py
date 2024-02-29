# -*- coding: utf-8 -*-
"""Linear Search implementation

The following code is the implementation of linear
search algorithm for an array of integer.

Other types can be searched using the same implementation
logic
"""
from typing import List

def linear_search(arr: List[int], key: int) -> int:
    """Linear search implementation to search element `key` in array `arr`.

    Parameters
    ----------
    arr
        Array or List in which key to be searched.
    key
        Element to be searched.

    Returns
    -------
    int
        index of the first element if found, -1 if not found.
    """
    l = len(arr)
    for i in range(l):
        if arr[i] == key:
            return i

    return -1
