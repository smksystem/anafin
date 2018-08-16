from tkinter import *

parent=Tk() # parent object
canvas = Canvas(parent, height=200) # a canvas in the parent object
frame = Frame(canvas) # a frame in the canvas
# a scrollbar in the parent
scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
# connect the canvas to the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y") # comment out this line to hide the scrollbar
canvas.pack(side="left", fill="both", expand=True) # pack the canvas
# make the frame a window in the canvas
canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")
# bind the frame to the scrollbar
frame.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
parent.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units')) # bind "Down" to scroll down
parent.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units')) # bind "Up" to scroll up
# bind the mousewheel to scroll up/down
parent.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))
labels = [Label(frame, text=str(i)) for i in range(20)] # make some Labels
for l in labels: l.pack() # pack them

parent.mainloop() # run program