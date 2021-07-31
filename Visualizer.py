#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:44:30 2021

@author: greg
"""


import tkinter as tk
import random, time



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
arr_length = 3
spd_scale_visible = False


visual_array = [x for x in range(1, 16)]
unsorted_array = visual_array.copy()
label_list = []

# Functions for buttons
def screen_reset():
    global unsorted_array
    for position, value in enumerate(unsorted_array):
        tk.Label(frm_graph_visual, height = value, width = 2).grid(row=0, column = position+1, padx = 1, sticky = "s")
    for position, value in enumerate(unsorted_array):
        tk.Label(frm_graph_visual, text = str(value), height = value, width = 2, bg = "red", fg = "white").grid(row=0, column = position+1, padx = 1, sticky = "s")
        
def bubble():
    global unsorted_array
    screen_reset()
    for i in range(len(unsorted_array)-1, 0, -1):
        tk.Label(frm_graph_visual, text = str(unsorted_array[i]), height = unsorted_array[i], width = 2, bg = "white", fg = "black").grid(row=0, column = i+1, padx = 1, sticky = "s")
        screen_reset()
        for j in range(i):
            #tk.Label(frm_graph_visual, text = str(unsorted_array[j]), height = unsorted_array[j], width = 2, bg = "white", fg = "black").grid(row=0, column = j+1, padx = 1, sticky = "s")
            if unsorted_array[j] > unsorted_array[j+1]:
                #tk.Label(frm_graph_visual, text = str(unsorted_array[j]), height = unsorted_array[j], width = 2, bg = "yellow", fg = "black").grid(row=0, column = j+1, padx = 1, sticky = "s")
                #tk.Label(frm_graph_visual, text = str(unsorted_array[i]), height = unsorted_array[i], width = 2, bg = "yellow", fg = "black").grid(row=0, column = i+1, padx = 1, sticky = "s")
                #time.sleep(0.2)
                #tk.Label(frm_graph_visual, height = unsorted_array[j], width = 2).grid(row=0, column = j+1, padx = 1, sticky = "s")
                #tk.Label(frm_graph_visual, height = unsorted_array[i], width = 2).grid(row=0, column = i+1, padx = 1, sticky = "s")
                temp = unsorted_array[j]
                unsorted_array[j] = unsorted_array[j+1]
                unsorted_array[j+1] = temp
                screen_reset()
                #tk.Label(frm_graph_visual, text = str(unsorted_array[j]), height = unsorted_array[j], width = 2, bg = "green", fg = "black").grid(row=0, column = j+1, padx = 1, sticky = "s")
                #tk.Label(frm_graph_visual, text = str(unsorted_array[i]), height = unsorted_array[i], width = 2, bg = "green", fg = "black").grid(row=0, column = i+1, padx = 1, sticky = "s")
                #time.sleep(0.2)
                #tk.Label(frm_graph_visual, text = str(unsorted_array[i]), height = unsorted_array[i], width = 2, bg = "red", fg = "black").grid(row=0, column = i+1, padx = 1, sticky = "s")
                #tk.Label(frm_graph_visual, text = str(unsorted_array[j]), height = unsorted_array[j], width = 2, bg = "red", fg = "black").grid(row=0, column = j+1, padx = 1, sticky = "s")
    screen_reset()
    print(unsorted_array)
def selection():
    pass

def insertion():
    pass

def speed_scale():        # Displays and hides the scale to control the algorithm speed
    global spd_scale_visible, unsorted_array
    if spd_scale_visible == True:
        scale_sort_speed.grid_forget()
        lbl_graph_space_end.grid(row = 0, column = len(unsorted_array)+1, sticky = "e") 
        spd_scale_visible = False
    else:    
        lbl_graph_space_end.grid_forget()
        scale_sort_speed.grid(column = len(unsorted_array)+1, sticky = "ns")
        spd_scale_visible = True
        
def reset_click():        # Clears the graph by changing colour of bars. Randomizes list. Displays list as vertical bars.
    global unsorted_array, visual_array, arr_length, lbl_graph_space_end
    for position, value in enumerate(unsorted_array):
        tk.Label(frm_graph_visual, height = value, width = 2).grid(row=0, column = position+1, padx = 1, sticky = "s")
    lbl_graph_space_end.grid_forget()
     
    arr_length = scale_array_size.get() + 1
    visual_array = [x for x in range(1, arr_length)]
    unsorted_array = visual_array.copy()
    random.shuffle(unsorted_array)
    lbl_graph_space_end.grid(row = 0, column = len(unsorted_array)+1, sticky = "e")  
    for position, value in enumerate(unsorted_array):
        tk.Label(frm_graph_visual, text = str(value), height = value, width = 2, bg = "red", fg = "white").grid(row=0, column = position+1, padx = 1, sticky = "s")
        


# Creates layout of GUI
frm_algorithms = tk.Frame(master = window)
frm_graph_visual = tk.Frame(master = window)
frm_number_scale = tk.Frame(master = window)
frm_speed_scale = tk.Frame(master = window)

frm_algorithms.grid(row = 0, sticky = "ew")
frm_graph_visual.grid(row = 1, sticky = "s", pady = 2) 
frm_speed_scale.grid(row = 2, pady = 1)
frm_number_scale.grid(row = 3, sticky = "ew", pady = 0)


# Widgets for GUI

# Sorting Algorithm selections
btn_bubble_sort = tk.Button(frm_algorithms, text = "Bubble Sort", command = bubble)
btn_insertion_sort = tk.Button(frm_algorithms, text = "Insertion Sort")
btn_selection_sort = tk.Button(frm_algorithms, text = "Selection Sort")

# Graph Spacing
lbl_graph_space_start = tk.Label(frm_graph_visual, width = 7)
lbl_graph_space_end = tk.Label(frm_graph_visual, width = 7)

# Bottom Widgets
btn_reset = tk.Button(frm_number_scale, text = "Randomize", command = reset_click)
scale_array_size = tk.Scale(frm_number_scale, from_ = 2, to = 100, orient=tk.HORIZONTAL, length = 100, variable = arr_length+1)
btn_speed = tk.Button(frm_number_scale, text="Speed", command = speed_scale)
scale_sort_speed = tk.Scale(frm_graph_visual, from_ = 100, to = 10, tickinterval = 10, orient = tk.VERTICAL)


# Displays the visual of the numbered list
for number in unsorted_array:
    tk.Label(frm_graph_visual, text = str(number), height = number, width = 2, bg = "red", fg = "white").grid(row=0, column = number, padx = 1, sticky = "s")
    
    
# Grid Functions  
    
# Sorting Algorithm selections
btn_bubble_sort.grid(row = 0, column = 0, padx = 5, sticky = "e")
btn_insertion_sort.grid(row = 0, column = 1, padx = 5, sticky = "ew")
btn_selection_sort.grid(row = 0, column = 2, padx = 5, sticky = "w")

# Graph Spacing
lbl_graph_space_start.grid(row = 0, column = 0, sticky = "w")
lbl_graph_space_end.grid(row = 0, column = len(unsorted_array)+1, sticky = "e") 

# Bottom Widgets 
btn_reset.grid(row = 0, column = 0)
scale_array_size.grid(row = 0, column = 1, padx = 75, sticky = "ew")
btn_speed.grid(row=0, column = 2)




window.mainloop()