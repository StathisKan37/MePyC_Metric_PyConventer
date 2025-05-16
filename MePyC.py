from tkinter import *
from tkinter.font import Font

# Creating the main application window
root = Tk()
root.title("Metric PyConventer")
#Setting the resizable property False
root.resizable(False, False)

def Convert():
	x = float(entry_1.get())
	result = (x * 1000)
	Label(root, text=result).grid(row=3, column=1)

# Label with font size 30 and bold weight
title_font = Font(size=20,weight="bold")
Label(root, text="Welcome to the Metric PyConventer", font=title_font).grid(row=0, column=0, columnspan=2)

# Labels definition
Label(root,text="Kilometers").grid(row=2, column=0)
Label(root,text="Meters").grid(row=2, column=1)

# Defining an entry
entry_1 = Entry(root, width=20)
entry_1.grid(row=3, column=0)
entry_1.insert(0, "0")

# Defining the convert button
Button(root, text="Convert", command=Convert, width=20).grid(row=4, column=0)

# Main event loop that keeps the window open and responsive
root.mainloop()
