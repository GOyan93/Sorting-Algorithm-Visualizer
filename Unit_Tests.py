#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 21:04:30 2021

@author: greg
"""
import unittest

# UNIT TEST FUNCTION
class testSorting(unittest.TestCase):
    
    # Determine sorting of a list of integers.
    def test_int_bubble_sort(self):
        unsorted_array = [random.randint(1, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array)
        
    def test_int_selection_sort(self):
        unsorted_array = [random.randint(1, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array)
        
    def test_int_insertion_sort(self):
        unsorted_array = [random.randint(1, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array)
        
        
            
        # Determine sorting of a list with integer 0
    def test__zero_int_bubble_sort(self):
        unsorted_array = [random.randint(0, 100000) for x in range(1, 100)]
        unsorted_array += [0]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array)
       
     def test__zero_int_selection_sort(self):
        unsorted_array = [random.randint(0, 100000) for x in range(1, 100)]
        unsorted_array += [0]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array)
        
     def test__zero_int_insertion_sort(self):
        unsorted_array = [random.randint(0, 100000) for x in range(1, 100)]
        unsorted_array += [0]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array)
        
        
        
        # Determine sorting of a list with negative integer.
    def test_neg_int_bubble_sort(self):
        unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array)
        
     def test_neg_int_selection_sort(self):
        unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array)
        
     def test_neg_int_insertion_sort(self):
        unsorted_array = [random.randint(-1000000, 100000) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array)
        
        
        # Determine sorting of a list with floating point numbers.
    def test_flt_bubble_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array)
        
    def test_flt_selection_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array)
        
    def test_flt_insertion_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array)
        
        
        # Determine sorting of a list with 0.0 floating point.
    def test_zero_flt_bubble_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array.append(0.0)
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array)
        
    def test_zero_flt_selection_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array.append(0.0)
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array)
        
    def test_zero_fltinsertion_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array.append(0.0)
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array)
        
        
        # Determine sorting of a list with negative floating point numbers.
    def test_neg_flt_bubble_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array)
        
    def test_neg_flt_selection_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array)
        
    def test_neg_flt_insertion_sort(self):
        unsorted_array = [random.random() for x in range(1, 100)]
        unsorted_array += [(random.random()*(-1)) for x in range(1, 100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array)
        
        
        # Determine sorting of a single digit list.
    def test_single_int_bubble_sort(self):
        unsorted_array = [random.randint(0,100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array)
        
     def test_single_int_selection_sort(self):
        unsorted_array = [random.randint(0,100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array)
        
     def test_single_int_binsertion_sort(self):
        unsorted_array = [random.randint(0,100)]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array)
           
        
        # Determine sorting of repeated integers.
    def test_repeat_int_bubble_sort(self):
        unsorted_array = [random.randint(0,1000) for x in range(100)]
        unsorted_array += [2, 3, 2, 10, 5, 10]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (bubble_sort(unsorted_array), sorted_array)
        
    def test_repeat_int_selection_sort(self):
        unsorted_array = [random.randint(0,1000) for x in range(100)]
        unsorted_array += [2, 3, 2, 10, 5, 10]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (selection_sort(unsorted_array), sorted_array)
        
    def test_repeat_int_insertion_sort(self):
        unsorted_array = [random.randint(0,1000) for x in range(100)]
        unsorted_array += [2, 3, 2, 10, 5, 10]
        sorted_array = sorted(unsorted_array)
        self.assertEqual (insertion_sort(unsorted_array), sorted_array)


if __name__ == '__main__':
    unittest.main() 


unsorted_array = [2,5,1,8,4,3]
#print(insertion_sort(unsorted_array)== sorted(unsorted_array))
#assert(insertion_sort(unsorted_array), sorted(unsorted_array)), "Last test Failed"