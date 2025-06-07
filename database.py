from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Vertical Separator Grid")

Label(root, text="Left Side").grid(row=0, column=0, padx=10)
# Vertical Separator
v_sep = ttk.Separator(root, orient='vertical')
v_sep.grid(row=0, column=1, sticky='ns', padx=5)
Label(root, text="Right Side").grid(row=0, column=2, padx=10)

root.mainloop()
