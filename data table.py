# Import the required libraries
from tkinter import *
from tkinter import ttk
import csv


# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("1920x1080")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(win, column=("Batch ID", "Timestamp", "Reading 1", "Reading 2", "Reading 3", "Reading 4", "Reading 5", "Reading 6", "Reading 7", "Reading 8", "Reading 9", "Reading 10"), show='headings', height=50)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Batch ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Timestamp")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Reading 1")

tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Reading 2")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="Reading 3")
tree.column("# 6", anchor=CENTER)
tree.heading("# 6", text="Reading 4")
tree.column("# 7", anchor=CENTER)
tree.heading("# 7", text="Reading 5")
tree.column("# 8", anchor=CENTER)
tree.heading("# 8", text="Reading 6")
tree.column("# 9", anchor=CENTER)
tree.heading("# 9", text="Reading 7")
tree.column("# 10", anchor=CENTER)
tree.heading("# 10", text="Reading 8")
tree.column("# 11", anchor=CENTER)
tree.heading("# 11", text="Reading 9")
tree.column("# 12", anchor=CENTER)
tree.heading("# 12", text="Reading 10")


with open("Data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for rows in csvreader:
        tree.insert('', 'end', text="1", values=(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10],rows[11]))


    

tree.pack()

win.mainloop()
