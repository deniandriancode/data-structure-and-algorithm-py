"""The following code show the implementation of array rotation"""

# rotate one by one
def rotate_obo_left(arr):
    """one by one"""
    tmp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]

    arr[len(arr)-1] = tmp
    return arr

def rotate_obo_right(arr):
    """one by one"""
    tmp = arr[len(arr)-1]
    for i in range(1, len(arr)):
        arr[len(arr)-i] = arr[len(arr)-i-1]

    arr[0] = tmp
    return arr


arr = [3, 5, 7, 8]
print(arr)
rot = rotate_obo_left(arr)
print(rot)

print()

arr = [3, 5, 7, 8]
print(arr)
rot = rotate_obo_right(arr)
rot = rotate_obo_right(rot)
print(rot)


# using temprary array
def rotate_tmp_left(arr, n):
    if n < 0:
        print("Come on man!")
        return
    n = n % len(arr)
    tmp_arr = []
    tmp_arr = arr[n:len(arr)] + arr[:n]
    return tmp_arr

def rotate_tmp_right(arr, n):
    if n < 0:
        print("Come on man!")
        return
    n = n % len(arr)
    tmp_arr = []
    tmp_arr = arr[len(arr)-n:] + arr[:len(arr)-n]
    return tmp_arr


print()
arr = [1, 2, 3, 4, 5, 6]
print(arr)
arr = rotate_tmp_left(arr, 7)
print(arr)

print()
arr = [1, 2, 3, 4, 5, 6]
print(arr)
arr = rotate_tmp_right(arr, 2)
print(arr)
