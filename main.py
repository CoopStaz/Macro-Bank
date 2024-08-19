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


# Define a function to load and resize images
def load_and_resize_image(filename, size=(100, 100)):
    try:
        img = Image.open(filename)
        img = img.resize(size, Image.NEAREST)  # Use LANCZOS for better quality
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image {filename}: {e}")
        return None


map_names = ['abyss', 'ascent', 'bind', 'breeze', 'fracture', 'haven', 'icebox', 'lotus', 'pearl', 'split', 'sunset']

# Store image references to prevent garbage collection
image_references = []

# Create a list of buttons
buttons = []
for i, map_name in enumerate(map_names):
    file_path = f"images/valorant_maps/{map_name}.png"
    new_img = load_and_resize_image(file_path)
    if new_img:  # Only create a button if the image was loaded successfully
        image_references.append(new_img)  # Keep a reference to the image
        button = Button(tk, image=new_img)
        button.grid(row=2 + i // 3, column=i % 3, padx=5, pady=5)
        buttons.append(button)  # Keep a reference to the button to prevent garbage collection

tk.mainloop()
