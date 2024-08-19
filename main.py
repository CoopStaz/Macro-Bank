from tkinter import *
from PIL import Image, ImageTk
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

record_title.grid(row=0, column=0, pady=10)
record_btn.grid(row=1, column=0)

map_names = ['abyss', 'ascent', 'bind', 'breeze', 'fracture', 'haven', 'icebox', 'lotus', 'pearl', 'split', 'sunset']


# Define a function to load and resize images
def load_and_resize_image(filename, size=(300, 300)):
    img = Image.open(f"images/valorant_maps/{filename}")
    img = img.resize(size, Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


tk.mainloop()
