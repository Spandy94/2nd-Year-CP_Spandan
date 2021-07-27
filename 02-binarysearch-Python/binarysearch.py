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

def binary_search(input_array, value):
    # Your code goes here
    low = 0 
    high = len(input_array)-1

    while low<=high:
        mid = (low+high)
        guess = input_array[mid]
        # found the element
        if guess == value:
            return mid
        # the guess was too high
        if guess > value:
            high = mid - 1
        # the guess was too lowP
        else:
            low = mid + 1
    # the item doesn't exist
    return -1
