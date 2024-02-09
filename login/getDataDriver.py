import tkinter as tk
from dataTree import create_data_tree
from storeData import get_table_data

def submit_data():
    data = get_table_data(table)
    print(data)
    # Further processing of data can be done here

app = tk.Tk()
app.title("Ingredient Input")

table = create_data_tree(app)
table.pack()

add_button = tk.Button(app, text="Add Row", command=lambda: table.insert('', 'end', values=["", ""]))
add_button.pack()

submit_button = tk.Button(app, text="Submit", command=submit_data)
submit_button.pack()

app.mainloop()
