from tkinter import *

root = Tk()
root.geometry("1430x840")
var1 = StringVar()

opt1 = OptionMenu(root, var1, 
                'Mockups', 
                'Assets', 
                'Symbols', 
                # here is where the separator should be
                'Trash')

opt1['menu'].insert_separator(3)

opt1.pack(side=LEFT, anchor=W)
var1.set('')

root.mainloop()