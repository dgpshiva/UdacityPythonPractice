"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    start = 0
    end = len(array) - 1
    if start < end:
        sortedArray = quickSortHelper(array, 0, len(array) - 1)
        return sortedArray
    else:
        return array

def quickSortHelper(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quickSortHelper(array, start, pivot - 1)
        quickSortHelper(array, pivot + 1, end)
    return array

def partition(array, start, end):
    i = start - 1
    pivot = array[end]

    for j in range(start, end + 1, 1):
        if array[j] <= pivot:
            i += 1
            if i < j:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp

    return i


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
