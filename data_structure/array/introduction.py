"""
The following code introduce the array data structure using builtin
Python module `array`.
"""

import array

# initialize array with signed integer typecode
arr = array.array('b', [4, 3, 5, 7, 6, 9, 8])

# Traversal
# print the original array
print("Original array :")
for i in range(len(arr)):
    print(arr[i], end=' ')

print()
print()

# Insertion
arr.insert(1, 88)
print("Array after insertion :")
for i in range(len(arr)):
    print(arr[i], end=' ')

print()
print()

# Appending
arr.append(0)
print("Array after append :")
for i in range(len(arr)):
    print(arr[i], end=' ')

print()
print()

# Pop
# pop the element at index 1
r = arr.pop(1)
print("Removed element is " + str(r))
print("Array after pop :")
for i in range(len(arr)):
    print(arr[i], end=' ')

print()
print()

# Remove
# remove the first occurence from the array
r = arr.remove(0)
print("Removed element is " + str(r))
print("Array after remove :")
for i in range(len(arr)):
    print(arr[i], end=' ')

print()
print()

# Index
# return the index of the first occurence of item in array
i = arr.index(5)
print("Found in index " + str(i))

# Reverse
print("Original array :")
for i in range(len(arr)):
    print(arr[i], end=' ')

print()
print()

arr.reverse()
print("Array after reverse :")
for i in range(len(arr)):
    print(arr[i], end=' ')

print()
print()
