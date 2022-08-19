import tkinter as tk
import subprocess
import sys
root= tk.Tk()
root.title('Download')
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot ():  
    
    subprocess.check_call([sys.executable, "ftp_download.py" + entry1.get()])
    #label1 = tk.Label(root, text= float(x1)**0.5)
    #canvas1.create_window(200, 230, window=label1)

def returnToMainMenu():
    subprocess.check_call([sys.executable, "Main Menu.py"])
    
    
button1 = tk.Button(text='Download (leave blank to get todays data', command=getSquareRoot)

button1.pack(
     ipadx=5,
    ipady=5,
    expand=True
)
#canvas1.create_window(200, 180, window=button1)

return_to_main_menu_button = tk.Button(
    root,
    text='Return to Main Menu',
    command=lambda:[root.destroy(),returnToMainMenu()]
)
return_to_main_menu_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
root.mainloop()
