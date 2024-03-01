"""The Selection sort algorithm is based on the idea
of finding the minimum or maximum element in an unsorted 
array and then putting it in its correct position in a sorted array.
"""
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def selection_sort(arr):
    l = 0
    r = len(arr)
    while l < r-1:
        minimum = l
        for i in range(l, r):
            if arr[i] < arr[minimum]:
                minimum = i

        swap(arr, l, minimum)
        l += 1

    return arr


if __name__ == "__main__":
    arr = [6, 5, 4, 8, 7, 1, 2, 4, 0, 9, 0, 8, 7, 9, 5, 4, 3, 6, 8, 7]
    print(arr)
    arr = selection_sort(arr)
    print(arr)
