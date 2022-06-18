import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("combox_test")


values = ["12개월","24개월","36개월"]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()


root.mainloop()