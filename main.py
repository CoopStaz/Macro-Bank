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

# Define all map images to PhotoImages
abyss_img = PhotoImage(file='images/valorant_maps/abyss.png')
ascent_img = PhotoImage(file='images/valorant_maps/ascent.png')
bind_img = PhotoImage(file='images/valorant_maps/bind.png')
breeze_img = PhotoImage(file='images/valorant_maps/breeze.png')
fracture_img = PhotoImage(file='images/valorant_maps/fracture.png')
haven_img = PhotoImage(file='images/valorant_maps/haven.png')
icebox_img = PhotoImage(file='images/valorant_maps/icebox.png')
lotus_img = PhotoImage(file='images/valorant_maps/lotus.png')
pearl_img = PhotoImage(file='images/valorant_maps/pearl.png')
split_img = PhotoImage(file='images/valorant_maps/split.png')
sunset_img = PhotoImage(file='images/valorant_maps/sunset.png')





tk.mainloop()
