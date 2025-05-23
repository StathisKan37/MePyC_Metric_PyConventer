from tkinter import *
from tkinter.font import Font
from functions import mass_function

# Creating the main application window
root = Tk()
root.title("Mass converter")
# Background color: #f0f0f0
root.configure(bg="#f0f0f0")
#Setting the resizable property False
root.resizable(False, False)

def Convert():
    try:
        x1 = float(entry_1.get())
        x2 = clicked_1.get()
        x3 = clicked_2.get()
        result = mass_function(x1, x2, x3)
    except ValueError:
        result = 'Please enter a valid number'
    
    result_label.config(text=result)

# Label with font size 30 and bold weight
title_font = Font(size=20,weight="bold")
Label(root, text="Welcome to the Mass PyConventer", font=title_font, bg="#f0f0f0").grid(row=0, column=0, columnspan=2, padx=10, pady=20)

# Defining the options
metric_options = [
	'Picograms (pg)',
	'Nanograms (ng)',
	'Micrograms (μg)',
	'Milligrams (mg)',
	'Grams (g)',
	'Kilograms (kg)',
	'Metric tons (t)',
	'Ounces (oz)',
	'Pounds (lb)',
	'Stones (st)',
	'US tons (short tons)',
	'UK tons (long tons)']

# Option menus
clicked_1 = StringVar()
clicked_1.set(metric_options[5])
clicked_2 = StringVar()
clicked_2.set(metric_options[8])

dropmenu_1 = OptionMenu(root, clicked_1, *metric_options)
dropmenu_2 = OptionMenu(root, clicked_2, *metric_options)
dropmenu_1.grid(row=2, column=0, pady=20)
dropmenu_2.grid(row=2, column=1, pady=20)

# Result label
result_label = Label(root, text='', bg="#f0f0f0")
result_label.grid(row=3, column=1)

# Defining an entry
entry_1 = Entry(root, width=20)
entry_1.grid(row=3, column=0)
entry_1.insert(0, "")

# Defining the convert button
Button(root, text="Convert", command=Convert, width=30, bg="#4CAF50", fg="white", activebackground="#45a049").grid(row=4, column=0, columnspan=2, pady=20)

# Main event loop that keeps the window open and responsive
root.mainloop()
