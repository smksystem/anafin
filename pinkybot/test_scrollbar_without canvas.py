import tkinter as tk
from tkinter import ttk

master=tk.Tk() 
f = tk.Frame(master,width=3)
f.grid(row=2, column=0, columnspan=8, rowspan=10, pady=30, padx=30)
f.config(width=5)

tree = ttk.Treeview(f, selectmode="extended")
scbHDirSel =tk.Scrollbar(f, orient=tk.HORIZONTAL, command=tree.xview)
scbVDirSel =tk.Scrollbar(f, orient=tk.VERTICAL, command=tree.yview)

tree.configure(yscrollcommand=scbVDirSel.set, xscrollcommand=scbHDirSel.set)           
# tree["columns"] = (columnListOutput)
tree.column("#0", width=40)
tree.heading("#0", text='SrNo', anchor='w')
tree.grid(row=2, column=0, sticky=tk.NSEW,in_=f, columnspan=10, rowspan=10)

scbVDirSel.grid(row=2, column=10, rowspan=10, sticky=tk.NS, in_=f)
scbHDirSel.grid(row=14, column=0, rowspan=2, sticky=tk.EW,in_=f)
f.rowconfigure(0, weight=1)
f.columnconfigure(0, weight=1)

master.mainloop()