import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, create one frame dimensions 200 by 200.
#
#   Use the default pack() method to place it in the window.
#
#   Also, place 3 labels in the frame labeling them as Label A, Label B, and
#   Label C and give them different background colors.
#
#   Use the place() method to place each of these labels at different
#   coordinates such that they do not overlap.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################
window = tk.Tk()
frame = tk.Frame(master=window, width=200, height=200, bg="lightgrey")
frame.pack()

labelA = tk.Label(master=frame, width=5, height=5, bg="red")
labelA.place(x=0,y=0)

labelB = tk.Label(master=frame, width=5, height=5, bg="white")
labelB.place(x=100,y=100)

labelC = tk.Label(master=frame, width=2, height=1, bg="blue")
labelC.place(x=175,y=17)

window.mainloop()