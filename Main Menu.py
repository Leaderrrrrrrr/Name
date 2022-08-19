import tkinter as tk
from tkinter import ttk
import subprocess
import sys
# root window
root = tk.Tk()
##win = tk.Tk()
root.geometry('1920x1080')
root.resizable(False, False)
root.title('Main Menu')

# exit button
def open_download():
    subprocess.check_call([sys.executable, "Download GUI.py"])
    




downloaded_files_button = ttk.Button(
    root,
    text='Downloaded Files',
    command=lambda: onClick()
)
downloaded_files_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

download_files_button = ttk.Button(
    root,
    text='Download Files',
    command=lambda:[root.destroy(),open_download()]
)
download_files_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda:[root.destroy()]
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#exit_button.place(x=100, y=500) 


root.mainloop()
