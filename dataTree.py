import tkinter as tk
from tkinter import ttk

def create_data_tree(app):
    table = ttk.Treeview(app, columns=(1, 2), show='headings', height=5)
    table.heading(1, text='Ingredient')
    table.heading(2, text='Quantity')
    return table
