# The follwoing code demonstrate how to reverse
# an array

def reverse_out_place(arr):
    """Reverse an array using extra array"""
    res = [None] * len(arr) # create a new identical array
    # traverse the original array starting from the last element
    for i in range(len(arr)):
        idx = len(arr)-i-1
        res[i] = arr[idx]

    return res

def reverse_in_place(arr):
    """Reverse an array without extra array"""
    l = 0
    r = len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return arr

arr = [8, 7, 6, 5, 3]
print("Original is " + str(arr))
res = reverse_out_place(arr)
print("Reversed is " + str(res))
print()

arr = [8, 7, 6, 5, 3]
print("Original is " + str(arr))
res = reverse_in_place(arr)
print("Reversed is " + str(res))
print()
