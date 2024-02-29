class Array:
    def __init__(self):
        pass

# No need to implement array on our own in Pyhton
# since Python has already native array data structure
# 
# We can however implement static array in Python in which
# the size of array is fixed

class StaticArray:
    def __init__(self, size):
        self.max_size = size
        self.elements = [None] * size
        self.size = 0

    def append(self, item):
        if self.size == self.max_size:
            raise IndexError("Array is full!")

        self.elements[self.size] = item
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Array is empty!")

        del self.elements[self.size-1]
        self.size -= 1

# The rest of operations very similar to what Python array provide

# Example
sa = StaticArray(3)
sa.append(1)
sa.append(1)
sa.append(1)
# sa.append(1) # error

sa.pop()
sa.pop()
sa.pop()
sa.pop() # error
