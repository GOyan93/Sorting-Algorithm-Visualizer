#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: Bubble Sort Algorithm
Created by: Greg Yandle
Date (DD/MM/YYYY): 09/07/2021 
"""

"""
The bubble sort algorithm will be used within a sorting visualizer.
This algorithm will take a list of numbers and will interate over the list 
bringing the highest value to the end of the list after each iteration.
The tests for this algorithm will use end cases involving the '0' integer, 
negative integers floating point numericals, and other inputs.
"""

import random



##########################
## BUBBLE SORT FUNCTION ##
##########################

def bubble_sort(arr):
    # Function iterates through array. Swapping highest values until length of list.
    # Function has linear complexity of O(N)
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
 

#############################
## SELECTION SORT FUNCTION ##
#############################
    
def selection_sort(arr):
    # Function iterates through array and takes either max or mix. Makes one swap
    # at the end of each iteration. 
    # Function has a exponential complexity of O(n^2)


####################
## TEST FUNCTIONS ##
####################
    
# Determine sorting of a list of integers.
unsorted_array = [random.randint(1, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Integer Test Failed."
    

# Determine sorting of a list with integer 0
unsorted_array = [random.randint(0, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Zero Test Failed."
    

# Determine sorting of a list with negative integer.
unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Negative Test Failed."


# Determine sorting of a list with floating point numbers.
unsorted_array = [random.random() for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Floating Point Test Failed."


# Determine sorting of a list with 0.0 floating point.
unsorted_array = [random.random() for x in range(1, 1000)]
unsorted_array.append(0.0)
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Floating Point Test Failed."
    

# Determine sorting of a list with negative floating point numbers.
unsorted_array = [random.random() for x in range(1, 1000)]
unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Floating Point Test Failed."
print(sorted_array)

# Determine sorting of a single digit list.
unsorted_array = [random.randint(0,1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Single Integer Test Failed."
    
