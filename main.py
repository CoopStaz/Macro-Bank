from tkinter import *

# Assign basic UI layout
tk = Tk()
tk.title("Macro Bank")
tk.configure(background="#bdeaff")
tk.minsize(600, 800)
tk.columnconfigure(0, weight=1)
tk.columnconfigure(1, weight=1)
tk.columnconfigure(2, weight=1)

record_title = Label(tk, text="Macro Recording")
record_title.grid(row=0, column=1, pady=10)

record_btn = Button(tk, text="Record", bg='red')
record_btn.grid(row=1, column=1)


tk.mainloop()
