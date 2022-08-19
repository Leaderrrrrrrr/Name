############################################
# Code for displaying the table using a gui
# after extracting the data from the csv file.
############################################

from tkinter import * # importing the tkinter module required for the gui
from tkinter import ttk # importing ttk from the tkinter module
import csv # imports the csv module
import glob

win = Tk() # Calls the function Tk() and assigns it to the variabe win


win.geometry("1920x1080") # Sets the size of the appilcation


style = ttk.Style() # Calls the Style() function and assigns it to the variable style
style.theme_use('clam') # Sets the theme to be clam

############################################ Creating the table fot the dataa
tree = ttk.Treeview(win, column=("Batch ID", "Timestamp", "Reading 1", "Reading 2", "Reading 3", "Reading 4", "Reading 5", "Reading 6", "Reading 7", "Reading 8", "Reading 9", "Reading 10"), show='headings', height=49) # Create the headings for each of the columns of the table.

tree.column("# 1", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 1", text="Batch ID") # Adds the text for the column name

tree.column("# 2", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 2", text="Timestamp") # Adds the text for the column name

tree.column("# 3", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 3", text="Reading 1") # Adds the text for the column name

tree.column("# 4", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 4", text="Reading 2") # Adds the text for the column name

tree.column("# 5", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 5", text="Reading 3") # Adds the text for the column name

tree.column("# 6", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 6", text="Reading 4") # Adds the text for the column name

tree.column("# 7", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 7", text="Reading 5") # Adds the text for the column name

tree.column("# 8", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 8", text="Reading 6") # Adds the text for the column name

tree.column("# 9", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 9", text="Reading 7") # Adds the text for the column name

tree.column("# 10", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 10", text="Reading 8") # Adds the text for the column name

tree.column("# 11", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 11", text="Reading 9") # Adds the text for the column name

tree.column("# 12", anchor=CENTER, width = 160) # Adds a column to the table
tree.heading("# 12", text="Reading 10") # Adds the text for the column name
############################################

for file in glob.glob('checked/*'):
    #open("MED_DATA_20210701153942.", 'r') as file: # Opens the csv file in read mode
    csvreader = csv.reader(open(file)) # Reads the csv file
    #header = next(csvreader) # Gets the headings for the columns from the csv file

    #tree.insert('', 'end', text="1", values=("batch_id","timestamp","reading1","reading2","reading3","reading4","reading5","reading6","reading7","reading8","reading9","reading10")) # Adds the data from one row of the 
    for rows in csvreader: # For loop for adding each row of data to the table to be displayed
        ##print(rows ==['batch_id', 'timestamp', 'reading1', 'reading2', 'reading3', 'reading4', 'reading5', 'reading6', 'reading7', 'reading8', 'reading9', 'reading10'])
        if rows != ['batch_id', 'timestamp', 'reading1', 'reading2', 'reading3', 'reading4', 'reading5', 'reading6', 'reading7', 'reading8', 'reading9', 'reading10']:
            
            tree.insert('', 'end', text="1", values=(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10],rows[-1])) # Adds the data from one row of the table
        


    

tree.pack()  # Calls the pack() function on tree.

win.mainloop() # Calls the mainloop() function on the variable win.
