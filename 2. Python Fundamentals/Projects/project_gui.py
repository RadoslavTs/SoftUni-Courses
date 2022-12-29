# from tkinter import *
# from tkinter.ttk import *

import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
greeting = tk.Label(text="Currency converter", width = 50, height = 4)
greeting.pack()
starting_currency_label = tk.Label(text="Input amount to convert", width = 50)
starting_currency_label.pack()
starting_currency_entry = tk.Entry(width = 50)
currency_to_convert = starting_currency_entry.get()
starting_currency_entry.pack()
blank_one = tk.Label(text="", width = 50, height = 1)
blank_one.pack()
starting_currency = starting_currency_entry.get()
button = tk.Button(text = "Convert", width = 50, height = 2)
button.pack()
blank_two = tk.Label(text="", width = 50, height = 1)
blank_two.pack()
converted_currency_label = tk.Label(text="Result", width = 50)
converted_currency_label.pack()
# converted_currency_result = tk.Label(currency_to_convert * 1.95585)
converted_currency_label.pack()
window.mainloop()
