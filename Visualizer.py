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
arr_length = 16
spd_scale_visible = False
dict_labels = {}
label_color = "blue"
text_color = "white"


# Creates list of values for dictionary assignement, [label key, value, column, bg color, fg color]
visual_array = [["label_bar_" + str(x), x, label_color, text_color]  for x in range(1, 16)]
unsorted_array = visual_array.copy()


# Functions for sorting buttons
        
def bubble():
    global unsorted_array
    global dict_labels
    screen_reset()
    for i in range(len(unsorted_array)-1, 0, -1):
        for j in range(i):
            unsorted_array[j][2] = "yellow"
            unsorted_array[j+1][2] = "yellow"
            screen_reset()
            if unsorted_array[j][1] > unsorted_array[j+1][1]:
                unsorted_array[j][2] = "red"
                unsorted_array[j+1][2] = "red"
                screen_reset()
                temp = unsorted_array[j][1]
                unsorted_array[j][1] = unsorted_array[j+1][1]
                unsorted_array[j+1][1] = temp
                screen_reset()  
            unsorted_array[j][2] = label_color
            unsorted_array[j+1][2] = label_color
            screen_reset()
        screen_reset()
    
def selection():
    global unosrted_array
    global dict_labels
    for i in range(len(unsorted_array)-1, 0, -1):
        position_of_max = 0
        for j in range(1, i+1):
            if unsorted_array[position_of_max][1] < unsorted_array[j][1]:
                position_of_max = j
            temp = unsorted_array[i]
            unsorted_array[i] = unsorted_array[position_of_max]
            unsorted_array[position_of_max] = temp
            screen_reset()
    screen_reset()

def insertion():
    global unsorted_array
    global dict_labels
    for i in range(1, len(unsorted_array)):
        current_value = unsorted_array[i]
        while i>0 and unsorted_array[i][1] < unsorted_array[i-1][1]:
            unsorted_array[i] = unsorted_array[i-1]
            i -= 1
            unsorted_array[i] = current_value
            screen_reset()
    screen_reset()
    
    
# Functions for clickable buttons.

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
    clear_screen()
    arr_length = scale_array_size.get() + 1
    visual_array = [["label_bar_" + str(x), x, label_color, text_color]  for x in range(1, arr_length)]
    unsorted_array = visual_array.copy()
    for x in range(len(unsorted_array)):
        random.shuffle(unsorted_array)
        lbl_graph_space_end.grid(row = 0, column = len(unsorted_array)+1, sticky = "e")  
    reset_dictionary()
    draw_screen()
        
    
# Functions for underlying processes
        
def reset_dictionary():         # Creates label objects within dictionary for storing label variables [Value, column, bg color, fg color, associated label object]
    global dict_labels, unsorted_array
    for position, item in enumerate(unsorted_array):
        dict_labels[item[0]] = [item[1], position+1, item[2], item[3], tk.Label(frm_graph_visual, text = str(item[1]), height = item[1], width = 2, bg = item[2], fg = item[3]) ]

def draw_screen():              # Iterates through the label list and calls the label associated with each item. 
    global dict_labels, unsorted_array
    for item in unsorted_array:  
        dict_labels[item[0]][4].grid(row=0, column = dict_labels[item[0]][1], padx = 1, sticky = "s")
    
def clear_screen():             # Iterates through the array and calls the destroy function on each assoicated label
    global dict_labels, unsorted_array
    for item in unsorted_array:
        dict_labels[item[0]][4].destroy() 

def screen_reset():             # Clears the visual, resets the label arguments, redraws the visual based off of the new label arguments
    global dict_labels, unsorted_array
    clear_screen()
    reset_dictionary()
    draw_screen()


# Creates layout of GUI
frm_algorithms = tk.Frame(master = window)
frm_graph_visual = tk.Frame(master = window)
frm_number_scale = tk.Frame(master = window)
frm_speed_scale = tk.Frame(master = window)

frm_algorithms.grid(row = 0, sticky = "ew")
frm_graph_visual.grid(row = 1, sticky = "s", pady = 2) 
frm_speed_scale.grid(row = 2, pady = 1)
frm_number_scale.grid(row = 3, sticky = "ew", pady = 0)

reset_dictionary()


# Widgets for GUI

# Sorting Algorithm selections
btn_bubble_sort = tk.Button(frm_algorithms, text = "Bubble Sort", command = bubble)
btn_insertion_sort = tk.Button(frm_algorithms, text = "Insertion Sort", command = insertion)
btn_selection_sort = tk.Button(frm_algorithms, text = "Selection Sort", command = selection)

# Graph Spacing
lbl_graph_space_start = tk.Label(frm_graph_visual, width = 7)
lbl_graph_space_end = tk.Label(frm_graph_visual, width = 7)

# Bottom Widgets
btn_reset = tk.Button(frm_number_scale, text = "Randomize", command = reset_click)
scale_array_size = tk.Scale(frm_number_scale, from_ = 2, to = 100, orient=tk.HORIZONTAL, length = 100, variable = arr_length+1)
btn_speed = tk.Button(frm_number_scale, text="Speed", command = speed_scale)
scale_sort_speed = tk.Scale(frm_graph_visual, from_ = 100, to = 10, tickinterval = 10, orient = tk.VERTICAL)


# Displays the visual of the numbered list
for item in unsorted_array:
    dict_labels[item[0]][4].grid(row=0, column = dict_labels[item[0]][1], padx = 1, sticky = "s")

    
    
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
scale_array_size.set(15)
btn_speed.grid(row=0, column = 2)




window.mainloop()
