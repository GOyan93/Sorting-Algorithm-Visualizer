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

import random, unittest
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
        for j in range(1, i+1):
            if arr[position_of_max] < arr[j]:
                position_of_max = j
            temp = arr[i]
            arr[i] = arr[position_of_max]
            arr[position_of_max] = temp
    return arr




def insertion_sort(arr):
    # Function creates sorted sublist as it iterates through the array.
    # Each item is compared then shuffled down the list until it is greater
    # than the previous item. 
    # Function has a linear complexity of O(n)
    for i in range(1, len(arr)):
        current_value = arr[i]
        while i>0 and arr[i] < arr[i-1]:
            arr[i] = arr[i-1]
            i -= 1
            arr[i] = current_value
    return arr
   







#if __name__ == '__main__':
#    unittest.main() 

# UNIT TEST FUNCTION
#TS = Unit_Tests.testSorting()
# Determine sorting of a list of integers.
#TS.test_int_bubble_sort()
#TS.test_int_selection_sort()
#TS.test_int_insertion_sort()
    
# Determine sorting of a list with integer 0
#TS.test_zero_int_bubble_sort()
#TS.test_zero_int_selection_sort()
#TS.test_zero_int_insertion_sort()


# Determine sorting of a list with negative integer.
#TS.test_neg_int_bubble_sort()
#TS.test_neg_int_selection_sort()
#TS.test_neg_int_insertion_sort()

# Determine sorting of a list with floating point numbers.
#TS.test_flt_bubble_sort()
#TS.test_flt_selection_sort()
#TS.test_flt_insertion_sort()

# Determine sorting of a list with 0.0 floating point.
#TS.test_zero_flt_bubble_sort()
#TS.test_zero_flt_selection_sort()
#TS.test_zero_flt_insertion_sort()

# Determine sorting of a list with negative floating point numbers.
#TS.test_neg_flt_bubble_sort()
#TS.test_neg_flt_selection_sort()
#TS.test_neg_flt_insertion_sort()

# Determine sorting of a single digit list.
#TS.test_single_int_bubble_sort()
#TS.test_single_int_selection_sort()
#TS.test_single_int_insertion_sort()

# Determine sorting of repeated integers.
#TS.test_repeat_int_bubble_sort()
#TS.test_repeat_int_selection_sort()
#TS.test_repeat_int_insertion_sort()


# Prints result of each sorting algorithm.
def algo_print():
    unsorted_arr = [random.randint(-1000, 1000) for x in range(10)]
    print(f"Unsorted List: {unsorted_arr}")
    print(f"Bubble Sort: {bubble_sort(unsorted_arr)}")
    print(f"Selection Sort: {selection_sort(unsorted_arr)}")
    print(f"Insertion Sort: {insertion_sort(unsorted_arr)}")
    
algo_print()

import unittest, random

# UNIT TEST FUNCTION
class testSorting(unittest.TestCase):
    
    # Determine sorting of a list of integers.
    def test_int_bubble_sort(self):
        unsorted_array = [random.randint(1, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array, "Bubble Sort: Integer Test Failed.")
        
    def test_int_selection_sort(self):
        unsorted_array = [random.randint(1, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array, "Selection Sort: Integer Test Failed.")
        
    def test_int_insertion_sort(self):
        unsorted_array = [random.randint(1, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array, "Insertion Sort: Integer Test Failed.")
        
        
            
        # Determine sorting of a list with integer 0
    def test_zero_int_bubble_sort(self):
        unsorted_array = [random.randint(0, 100000) for x in range(1, 100)]
        unsorted_array += [0]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array, "Bubble Sort: Zero Test Failed.")
       
    def test_zero_int_selection_sort(self):
        unsorted_array = [random.randint(0, 100000) for x in range(1, 100)]
        unsorted_array += [0]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array, "Selection Sort: Zero Test Failed.")
        
    def test_zero_int_insertion_sort(self):
        unsorted_array = [random.randint(0, 100000) for x in range(1, 100)]
        unsorted_array += [0]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array, "Insertion Sort: Zero Test Failed.")
        
        
        
        # Determine sorting of a list with negative integer.
    def test_neg_int_bubble_sort(self):
        unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array, "Bubble Sort: Negative Test Failed.")
        
    def test_neg_int_selection_sort(self):
        unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array, "Selection Sort: Negative Test Failed.")
        
    def test_neg_int_insertion_sort(self):
        unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array, "Insertion Sort: Negative Test Failed.")
        
        
        # Determine sorting of a list with floating point numbers.
    def test_flt_bubble_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array, "Bubble Sort: Floating Point Test Failed.")
        
    def test_flt_selection_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array, "Selection Sort: Floating Point Test Failed.")
        
    def test_flt_insertion_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array, "Insertion Sort: Floating Point Test Failed.")
        
        
        # Determine sorting of a list with 0.0 floating point.
    def test_zero_flt_bubble_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array.append(0.0)
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array, "Bubble Sort: Zero Floating Point Test Failed.")
        
    def test_zero_flt_selection_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array.append(0.0)
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array, "Selection Sort: Zero Floating Point Test Failed.")
        
    def test_zero_flt_insertion_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array.append(0.0)
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array, "Insertion Sort: Zero Floating Point Test Failed.")
        
        
        # Determine sorting of a list with negative floating point numbers.
    def test_neg_flt_bubble_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array, "Bubble Sort: Negative Floating Point Test Failed.")
        
    def test_neg_flt_selection_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array, "Selection Sort: Negative Floating Point Test Failed.")
        
    def test_neg_flt_insertion_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array, "Insertion Sort: Negative Floating Point Test Failed.")
        
        
        # Determine sorting of a single digit list.
    def test_single_int_bubble_sort(self):
        unsorted_array = [random.randint(0,100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array, "Bubble Sort: Single Integer Test Failed.")
        
    def test_single_int_selection_sort(self):
        unsorted_array = [random.randint(0,100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array, "Selection Sort: Single Integer Test Failed.")
        
    def test_single_int_insertion_sort(self):
        unsorted_array = [random.randint(0,100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array, "Insertion Sort: Single Integer Test Failed.")
           
        
        # Determine sorting of repeated integers.
    def test_repeat_int_bubble_sort(self):
        unsorted_array = [random.randint(0,1000) for x in range(100)]
        unsorted_array += [2, 3, 2, 10, 5, 10]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array, "Bubble Sort: Repeated Integer Test Failed.")
        
    def test_repeat_int_selection_sort(self):
        unsorted_array = [random.randint(0,1000) for x in range(100)]
        unsorted_array += [2, 3, 2, 10, 5, 10]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array, "Selection Sort: Repeated Integer Test Failed.")
        
    def test_repeat_int_insertion_sort(self):
        unsorted_array = [random.randint(0,1000) for x in range(100)]
        unsorted_array += [2, 3, 2, 10, 5, 10]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array, "Insertion Sort: Repeated Integer Test Failed.")


if __name__ == '__main__':
    unittest.main() 
    
#algo_print()