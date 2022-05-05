"""
Program: Converter GUI using TKinter
Author: Subhashish Dhar
Date: 03/09/2021
"""

from tkinter import Tk, Label, Entry, Button


# Defining the button click action
def convert_miles_to_km():
    """converts miles to km"""
    distance_miles = miles_entry.get()
    distance_km = round(int(distance_miles) * 1.6)
    result_label.config(text=distance_km)


# Creating the window object
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

# Creating the label objects
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

eq_label = Label(text="is equal to")
eq_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

# Creating the entry object
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

# Creating the button object
calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
