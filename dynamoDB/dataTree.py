import tkinter as tk
from tkinter import ttk
#This creates a display for people to put ingredients and the quantity
def create_data_tree(app):
    table = ttk.Treeview(app, columns=(1, 2), show='headings', height=5)
    table.heading(1, text='Ingredient')
    table.heading(2, text='Quantity')
    return table

