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
 



    

