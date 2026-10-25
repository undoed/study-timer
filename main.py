import tkinter as tk

wn = tk.Tk()
wn.geometry("650x500")
wn.config(bg="white")

# Label for starting from 0 or custom starting time
starting_time_label = tk.Label()
starting_time_label.config(text="Would you like to set a custom starting time, \nor start from 0?")
starting_time_label.config(font=("Arial", 16, "bold"))
starting_time_label.config(bg="white")
starting_time_label.place(x=100, y=100)

# Start from 0 button
start_from_zero = tk.Button()
start_from_zero.config(text="Start From 0")
start_from_zero.place(x=280, y=210)

# Start from custom time button
start_from_zero = tk.Button()
start_from_zero.config(text="Set Custom Starting Time")
start_from_zero.place(x=240, y=260)

wn.mainloop()