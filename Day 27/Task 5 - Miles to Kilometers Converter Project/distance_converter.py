from tkinter import *

def converter():
    miles = miles_input.get()
    kms = round(float(miles)*1.609, 2)
    kilometres_result_label.config(text=f"{kms}")


window = Tk()
window.title("Miles to Kilometres Converter")
window.minsize(width=350, height=100)
window.config(padx=80, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometres_result_label = Label(text="0")
kilometres_result_label.grid(column=1, row=1)

kilometres_label = Label(text="Kms")
kilometres_label.grid(column=2, row=1)

convert_button = Button(text="Convert", command=converter)
convert_button.grid(column=1, row=2)

window.mainloop()
