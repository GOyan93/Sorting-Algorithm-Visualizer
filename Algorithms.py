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



# SORTING FUNCTIONS

def bubble_sort(arr):
    # Function iterates through array. Swapping highest values until length of list.
    # Function has an exponential complexity of O(n^2)
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
 


def selection_sort(arr):
    # Function iterates through array and takes either max or mix. Makes one swap
    # at the end of each iteration. 
    # Function has an exponential complexity of O(n^2)
    for i in range(len(arr)-1, 0, -1):
        position_of_max = 0
        for j in range(i, len(arr)-1):
            if arr[position_of_max] < arr[j]:
                position_of_max = j
            temp = arr[j]
            arr[j] = arr[position_of_max]
            arr[position_of_max] = temp
    return arr



def insertion_sort(arr):
    # Function creates sorted sublist as it iterates through the array.
    # Each item is compared then shuffled down the list until it is greater
    # than the previous item. 
    # Function has a linear complexity of O(n)
    for i in range(1, len(arr)-1):
        while arr[i] < arr[i-1]:
            pass
            

# UNIT TEST FUNCTION
    
# Determine sorting of a list of integers.
unsorted_array = [random.randint(1, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Integer Test Failed."
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Integer Test Failed."

# Determine sorting of a list with integer 0
unsorted_array = [random.randint(0, 100000) for x in range(1, 1000)]
unsorted_array += [0]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Zero Test Failed."
assert(bubble_sort(unsorted_array) == sorted_array), "Selection Sort: Zero Test Failed."


# Determine sorting of a list with negative integer.
unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Negative Test Failed."
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Negative Test Failed."


# Determine sorting of a list with floating point numbers.
unsorted_array = [random.random() for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Floating Point Test Failed."
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Floating Point Test Failed."

# Determine sorting of a list with 0.0 floating point.
unsorted_array = [random.random() for x in range(1, 1000)]
unsorted_array.append(0.0)
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Floating Point Test Failed."
assert(bubble_sort(unsorted_array) == sorted_array), "Selection Sort: Floating Point Test Failed."


# Determine sorting of a list with negative floating point numbers.
unsorted_array = [random.random() for x in range(1, 1000)]
unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Negative Floating Point Test Failed."
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Negative Floating Point Test Failed."



# Determine sorting of a single digit list.
unsorted_array = [random.randint(0,1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Single Integer Test Failed."
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Single Integer Test Failed."
    

# Determine sorting of repeated integers.
unsorted_array = [random.randint(0,1000) for x in range(1000)]
unsorted_array += [2, 3, 2, 10, 5, 10]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Single Integer Test Failed."
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Single Integer Test Failed."


# Prints result of each sorting algorithm.
def algo_print():
    unsorted_arr = [random.randint(-1000, 1000) for x in range(10)]
    print(f"Unsorted List: {unsorted_arr}")
    print(f"Bubble Sort: {bubble_sort(unsorted_arr)}")
    print(f"Selection Sort: {selection_sort(unsorted_arr)}")
    
algo_print()