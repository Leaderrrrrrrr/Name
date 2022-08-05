import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
win = tk.Tk()
root.geometry('1920x1080')
root.resizable(False, False)
root.title('Button Demo')

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

exit_button.place(x=100, y=500) 


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

root.mainloop()
