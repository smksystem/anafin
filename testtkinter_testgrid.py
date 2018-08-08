import tkinter as tk
from tkinter import N, S, W, E,RIGHT
from tkinter import ttk

class MyWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent,width=100,height=200)
        # tk.Frame.grid_propagate(0)
        # parent.grid_columnconfigure(0, weight=1)

        label = tk.Label(self, text="Hello, world",borderwidth=3, relief="groove")
        label.grid(row=0,column=0)

        label = tk.Label(self, text="Hello, world",borderwidth=2, relief="groove")
        label.grid(row=1,column=0)

        label.bind("<1>", self.quit)


        button = tk.Button(self,text="Start Login")
        
        button.grid(row=0, column=0, sticky="WENS")

    def quit(self, event=None):
        sys.exit()

root = tk.Tk()
root.geometry("800x480")
MyWindow(root).pack()
root.mainloop()