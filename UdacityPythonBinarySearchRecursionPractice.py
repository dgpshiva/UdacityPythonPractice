"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

import math

def binary_search(input_array, value):
    """Your code goes here."""
    length = len(input_array)
    if length%2 == 0:
        middle = int(math.floor(length/2)) - 1
    else:
        middle = int(math.floor(length/2))

    if input_array[middle] == value:
        return middle
    elif length>1 and value > input_array[middle]:
        new_array = []
        for i in range(middle+1, length):
            new_array.append(input_array[i])
        if binary_search(new_array, value) > -1:
            return input_array.index(value)
    elif length>1 and value < input_array[middle]:
        new_array = []
        for i in range(0, middle):
            new_array.append(input_array[i])
        if binary_search(new_array, value) > -1:
            return input_array.index(value)

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)