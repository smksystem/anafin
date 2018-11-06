from tkinter import *

root=Tk()

frame=Frame(root,width=300,height=300)
frame.grid(row=0,column=0)


canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))

# btnBuyCommand=Button(canvas,text="Buy Now", width = 2,height=2)
# btnBuyCommand.grid(row=0,column=0,sticky="w")
# btnBuyCommand.pack(side=RIGHT,fill=X)

hbar=Scrollbar(frame,orient=HORIZONTAL,command=canvas.xview)
hbar.grid(row=0,column=0)
# hbar.pack(side=BOTTOM,fill=X)
# hbar.config()

vbar=Scrollbar(frame,orient=VERTICAL,command=canvas.yview)
# vbar.pack(side=RIGHT,fill=Y)
vbar.grid(row=1,column=0)
# vbar.config()

canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.grid(row=0,column=0)
# canvas.pack(side=LEFT,expand=True,fill=BOTH)

root.mainloop()