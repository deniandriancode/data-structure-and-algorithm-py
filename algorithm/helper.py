"""
Helper modules to work with various algorithms
"""

from typing import List
import random

def gen_randint(l: int, r: int, n: int) -> List[int]:
    """Generate a random n elements array of integer from l to r (inclusive)"""
    arr = []
    for _ in range(n):
        arr.append(random.randint(l, r))

    return arr

def gen_randfloat(l: float, r: float, n: int) -> List[float]:
    """Generate a random n elements array of float numbers from l to r"""
    arr = []
    for _ in range(n):
        arr.append(random.uniform(l, r))

    return arr
