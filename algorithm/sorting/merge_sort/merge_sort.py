import sys
sys.path.append(".")
import algorithm.helper as h

def merge_sort(arr):
    """Merge sort implementation"""
    if len(arr) > 1:
        mid = len(arr) // 2
        l_arr = arr[:mid]
        r_arr = arr[mid:]

        merge_sort(l_arr)
        merge_sort(r_arr)

        i = j = k = 0

        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] <= r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1

        # check if any element was left
        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1


if __name__ == "__main__":
    arr = h.gen_randint(0, 10, 10)
    print(arr)
    merge_sort(arr)
    print(arr)
