#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 21:04:30 2021

@author: greg
"""


# UNIT TEST FUNCTION
    
# Determine sorting of a list of integers.
unsorted_array = [random.randint(1, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert bubble_sort(unsorted_array) == sorted_array, "Bubble Sort: Integer Test Failed."
unsorted_array = [random.randint(1, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert selection_sort(unsorted_array) == sorted_array, "Selection Sort: Integer Test Failed."
unsorted_array = [random.randint(1, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert insertion_sort(unsorted_array) == sorted_array, "Insertion Sort: Integer Test Failed."
unsorted_array = [random.randint(1, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)

    
# Determine sorting of a list with integer 0
unsorted_array = [random.randint(0, 100000) for x in range(1, 1000)]
unsorted_array += [0]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Zero Test Failed."
unsorted_array = [random.randint(0, 100000) for x in range(1, 1000)]
unsorted_array += [0]
sorted_array = sorted(unsorted_array)
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Zero Test Failed."
unsorted_array = [random.randint(0, 100000) for x in range(1, 1000)]
unsorted_array += [0]
sorted_array = sorted(unsorted_array)
assert(insertion_sort(unsorted_array) == sorted_array), "Insertion Sort: Zero Test Failed."


# Determine sorting of a list with negative integer.
unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Negative Test Failed."
unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Negative Test Failed."
unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(insertion_sort(unsorted_array) == sorted_array), "Insertion Sort: Negative Test Failed."


# Determine sorting of a list with floating point numbers.
unsorted_array = [random.random() for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Floating Point Test Failed."
unsorted_array = [random.random() for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Floating Point Test Failed."
unsorted_array = [random.random() for x in range(1, 1000)]
sorted_array = sorted(unsorted_array)
assert(insertion_sort(unsorted_array) == sorted_array), "Insertion Sort: Floating Point Test Failed."


# Determine sorting of a list with 0.0 floating point.
unsorted_array = [random.random() for x in range(1, 1000)]
unsorted_array.append(0.0)
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Floating Point Test Failed."
unsorted_array = [random.random() for x in range(1, 1000)]
unsorted_array.append(0.0)
sorted_array = sorted(unsorted_array)
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Floating Point Test Failed."
unsorted_array = [random.random() for x in range(1, 1000)]
unsorted_array.append(0.0)
sorted_array = sorted(unsorted_array)
assert(insertion_sort(unsorted_array) == sorted_array), "Insertion Sort: Floating Point Test Failed."


# Determine sorting of a list with negative floating point numbers.
unsorted_array = [random.random() for x in range(1, 1000)]
unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Negative Floating Point Test Failed."
unsorted_array = [random.random() for x in range(1, 1000)]
unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
sorted_array = sorted(unsorted_array)
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Negative Floating Point Test Failed."
unsorted_array = [random.random() for x in range(1, 1000)]
unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
sorted_array = sorted(unsorted_array)
assert(insertion_sort(unsorted_array) == sorted_array), "Insertion Sort: Negative Floating Point Test Failed."


# Determine sorting of a single digit list.
unsorted_array = [random.randint(0,1000)]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Single Integer Test Failed."
unsorted_array = [random.randint(0,1000)]
sorted_array = sorted(unsorted_array)
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Single Integer Test Failed."
unsorted_array = [random.randint(0,1000)]
sorted_array = sorted(unsorted_array)
assert(insertion_sort(unsorted_array) == sorted_array), "Insertion Sort: Single Integer Test Failed."
   

# Determine sorting of repeated integers.
unsorted_array = [random.randint(0,1000) for x in range(1000)]
unsorted_array += [2, 3, 2, 10, 5, 10]
sorted_array = sorted(unsorted_array)
assert(bubble_sort(unsorted_array) == sorted_array), "Bubble Sort: Repeated Integer Test Failed."
unsorted_array = [random.randint(0,1000) for x in range(1000)]
unsorted_array += [2, 3, 2, 10, 5, 10]
sorted_array = sorted(unsorted_array)
assert(selection_sort(unsorted_array) == sorted_array), "Selection Sort: Repeated Integer Test Failed."
unsorted_array = [random.randint(0,1000) for x in range(1000)]
unsorted_array += [2, 3, 2, 10, 5, 10]
sorted_array = sorted(unsorted_array)
assert(insertion_sort(unsorted_array) == sorted_array), "Insertion Sort: Repeated Integer Test Failed."


# Prints result of each sorting algorithm.
def algo_print():
    unsorted_arr = [random.randint(-1000, 1000) for x in range(10)]
    print(f"Unsorted List: {unsorted_arr}")
    print(f"Bubble Sort: {bubble_sort(unsorted_arr)}")
    print(f"Selection Sort: {selection_sort(unsorted_arr)}")
    print(f"Insertion Sort: {insertion_sort(unsorted_arr)}")
    
#algo_print()
unsorted_array = [2,5,1,8,4,3]
#print(insertion_sort(unsorted_array)== sorted(unsorted_array))
#assert(insertion_sort(unsorted_array), sorted(unsorted_array)), "Last test Failed"