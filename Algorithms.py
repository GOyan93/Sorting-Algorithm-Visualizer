#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: Algorithms
Created by: Greg Yandle
Date (DD/MM/YYYY): 09/07/2021 
"""

"""
Various sorting algorithms to be used within a sorting algorithm visualizer. 
"""

import random
import Unit_Tests



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
    for i in range(1, len(arr)):
        while  arr[i] < arr[i-1]:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
    return arr
            

# UNIT TEST FUNCTION
    
# Determine sorting of a list of integers.


    
# Determine sorting of a list with integer 0



# Determine sorting of a list with negative integer.



# Determine sorting of a list with floating point numbers.


# Determine sorting of a list with 0.0 floating point.



# Determine sorting of a list with negative floating point numbers.



# Determine sorting of a single digit list.


# Determine sorting of repeated integers.



# Prints result of each sorting algorithm.
def algo_print():
    unsorted_arr = [random.randint(-1000, 1000) for x in range(10)]
    print(f"Unsorted List: {unsorted_arr}")
    print(f"Bubble Sort: {bubble_sort(unsorted_arr)}")
    print(f"Selection Sort: {selection_sort(unsorted_arr)}")
    print(f"Insertion Sort: {insertion_sort(unsorted_arr)}")
    
algo_print()

