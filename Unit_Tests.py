#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 21:04:30 2021

@author: greg
"""
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


unsorted_array = [2,5,1,8,4,3]
#print(insertion_sort(unsorted_array)== sorted(unsorted_array))
#assert(insertion_sort(unsorted_array), sorted(unsorted_array)), "Last test Failed"