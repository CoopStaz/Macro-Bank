from tkinter import *
from record_macro import Recorder

# Assign basic UI layout
tk = Tk()
tk.title("Macro Bank")
tk.configure(background="#bdeaff")
tk.minsize(600, 800)
tk.columnconfigure(0, weight=1)
tk.columnconfigure(1, weight=1)
tk.columnconfigure(2, weight=1)

# Initialise recorder class
recorder = Recorder()

record_title = Label(tk, text="Macro Recording")
record_btn = Button(tk, text="Record", bg='red', command=recorder.record)

record_title.grid(row=0, column=1, pady=10)
record_btn.grid(row=1, column=1)



tk.mainloop()
