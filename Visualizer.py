#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:44:30 2021

@author: greg
"""


import tkinter as tk

# Creates window for GUI
window = tk.Tk()
window.title("Sorting Algorithm Visualizer")

# Configure window
window.rowconfigure(0, minsize = 50, weight = 1)
window.rowconfigure(1, minsize = 400, weight = 1)
window.rowconfigure(2, minsize = 50, weight = 1)

# Creates layout of GUI
frm_algorithms = tk.Frame(master = window)
frm_graph_visual = tk.Frame(master = window)
frm_number_slider = tk.Frame(master = window)

# Buttons for GUI
btn_bubble_sort = tk.Button(frm_algorithms, text = "Bubble Sort")
btn_insertion_sort = tk.Button(frm_algorithms, text = "Insertion Sort")
btn_selection_sort = tk.Button(frm_algorithms, text = "Selection Sort")
btn_reset = tk.Button(frm_number_slider, text = "Reset")

btn_bubble_sort.grid(row = 0, column = 0, padx = 2)
btn_insertion_sort.grid(row = 0, column = 1, padx = 2)
btn_selection_sort.grid(row = 0, column = 2, padx = 2)
btn_reset.grid(row = 0, column = 0, padx = 2)



window.mainloop()