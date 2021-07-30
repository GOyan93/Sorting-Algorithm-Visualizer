#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:44:30 2021

@author: greg
"""


import tkinter as tk
import random



# Creates window for GUI
window = tk.Tk()
window.title("Sorting Algorithm Visualizer")

# Configure window
window.rowconfigure(0, minsize = 50, weight = 1)
window.rowconfigure(1, minsize = 200, weight = 1)
window.rowconfigure(2, minsize = 50)
window.rowconfigure(3, minsize = 50, weight = 1)

# Variables
speed = tk.DoubleVar()
arr_length = tk.IntVar()
arr_length = 2
spd_slide_visible = False


visual_array = [x for x in range(1, 16)]
unsorted_array = visual_array.copy()


# Functions for buttons
def bubble():
    pass

def selection():
    pass

def insertion():
    pass

def speed_slide():
    global spd_slide_visible
    if spd_slide_visible == True:
        slider_sort_speed.pack_forget()
        spd_slide_visible = False
    else:    
        slider_sort_speed.pack(side = "right")
        spd_slide_visible = True
        
def reset_click():
    unsorted_array = random.shuffle(visual_array)
    for number in unsorted_array:
        tk.Label(frm_graph_visual, text = str(number), height = number, width = 2, bg = "red", fg = "white").grid(row=0, column = number, padx = 1, sticky = "s")
    
    
            



# Creates layout of GUI
frm_algorithms = tk.Frame(master = window)
frm_graph_visual = tk.Frame(master = window)
frm_number_slider = tk.Frame(master = window)
frm_speed_slider = tk.Frame(master = window)

frm_algorithms.grid(row = 0, sticky = "ew")
frm_graph_visual.grid(row = 1, sticky = "nsew", pady = 2) 
frm_speed_slider.grid(row = 2, pady = 1)
frm_number_slider.grid(row = 3, sticky = "ew", pady = 0)


# Widgets for GUI
btn_bubble_sort = tk.Button(frm_algorithms, text = "Bubble Sort")
btn_insertion_sort = tk.Button(frm_algorithms, text = "Insertion Sort")
btn_selection_sort = tk.Button(frm_algorithms, text = "Selection Sort")
lbl_graph_space_1 = tk.Label(frm_graph_visual, width = 7)

btn_reset = tk.Button(frm_number_slider, text = "Randomize", command = reset_click)
sldr_arr_size = tk.Scale(frm_number_slider, from_ = 2, to = 200, orient=tk.HORIZONTAL, length = 100, variable = arr_length, state="disabled")
btn_speed = tk.Button(frm_number_slider, text="Speed", command = speed_slide, state="disabled")
slider_sort_speed = tk.Scale(frm_speed_slider, from_ = 1, to = 10, orient = tk.VERTICAL, state="disabled")

for number in unsorted_array:
    tk.Label(frm_graph_visual, text = str(number), height = number, width = 2, bg = "red", fg = "white").grid(row=0, column = number, padx = 1, sticky = "s")
    
#tk.Label(frm_graph_visual, text = str(arr_length), height = arr_length, width = 2, bg = "red", fg = "white" ).grid(row=0, column = 0, padx = 1)

btn_bubble_sort.grid(row = 0, column = 0, padx = 5, sticky = "e")
btn_insertion_sort.grid(row = 0, column = 1, padx = 5, sticky = "ew")
btn_selection_sort.grid(row = 0, column = 2, padx = 5, sticky = "w")
lbl_graph_space_1.grid(row = 0, column = 0, sticky = "w")
btn_reset.grid(row = 0, column = 0)
sldr_arr_size.grid(row = 0, column = 1, padx = 75, sticky = "ew")
btn_speed.grid(row=0, column = 2)




window.mainloop()