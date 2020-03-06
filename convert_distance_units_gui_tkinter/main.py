import tkinter as tk
from tkinter import ttk 

def convert_feet_to_meters(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


def convert_meters_to_feet(*args):
    try:
        value = float(meters2.get())
        feet2.set((value / 0.3048) - (-0.5/30480))
    except ValueError:
        pass

root = tk.Tk()
root.title('Feet to Meters and Vice Versa')

mainframe = tk.ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = tk.StringVar()
meters = tk.StringVar()

feet_entry = tk.ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

tk.ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(tk.W, tk.E))
tk.ttk.Button(mainframe, text="Calculate", command=convert_feet_to_meters).grid(column=3, row=3, sticky=tk.W)

tk.ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=tk.W)
tk.ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=tk.E)
tk.ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=tk.W)

feet2 = tk.StringVar()
meters2 = tk.StringVar()

feet_entry2 = tk.ttk.Entry(mainframe, width=7, textvariable=meters2)
feet_entry2.grid(column=2, row=4, sticky=(tk.W, tk.E))

tk.ttk.Label(mainframe, text="meters").grid(column=3, row=4, sticky=tk.W)
tk.ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=5, sticky=tk.W)
tk.ttk.Label(mainframe, textvariable=feet2).grid(column=2, row=5, sticky=(tk.W, tk.E)   )
tk.ttk.Label(mainframe, text="feet").grid(column=3, row=5, sticky=tk.W)
tk.ttk.Button(mainframe, text="Calculate", command=convert_meters_to_feet).grid(column=3, row=6, sticky=tk.W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', convert_feet_to_meters)

root.mainloop()
