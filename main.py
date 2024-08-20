from tkinter import *
from PIL import Image, ImageTk
from record_macro import Recorder
import json

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

title_label = Label(text='VALORANT Maps', font=("New Amsterdam", 16, 'bold'), bg="#bdeaff", pady=8)
title_label.grid(columnspan=3, row=0, column=0)


# Function to switch to macro management page
def open_map_page(map_name):
    # Hide the main page widgets
    for widget in tk.winfo_children():
        if isinstance(widget, Toplevel):
            continue  # Skips Toplevel windows
        widget.grid_forget()

    # TODO Create better styling for the map pages
    # TODO Create better styling of new macros widget
    # TODO Create better layout and styling of the stored macros

    # Create a new frame for the map page
    map_page = Frame(tk, bg="#bdeaff")
    map_page.grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Centers the widgets properly
    map_page.columnconfigure(0, weight=1)
    map_page.columnconfigure(1, weight=1)
    map_page.columnconfigure(2, weight=1)

    # Label for the selected map
    label = Label(map_page, text=f"Macros for {map_name.capitalize()}", bg="#bdeaff", font=("New Amsterdam", 16, 'bold'))
    label.grid(row=0, column=0, pady=10, columnspan=3)

    # Button to create a new macro
    create_macro_btn = Button(map_page, text="Create New Macro", bg='red', fg='white',
                              font=("New Amsterdam", 12, 'bold'),
                              command=lambda: create_macro(map_name))
    create_macro_btn.grid(row=1, column=0, pady=10, columnspan=3)

    # Listbox to display saved macros
    macros_list = Listbox(map_page, width=50, height=20, font=("New Amsterdam", 12))
    macros_list.grid(row=2, column=0, columnspan=3, pady=10)

    # Load and display saved macros for the map
    load_macros(map_name, macros_list)


# Function to create a new macro
def create_macro(map_name):
    def start_recording():
        macro_name = entry.get()
        if not macro_name:
            print("Macro name cannot be empty.")
            return

        # Start recording and pass the macro name and map name
        recorder.record(macro_name, map_name)

        # Close the create macro window
        create_macro_win.destroy()

        print(f"Macro '{macro_name}' saved for {map_name.capitalize()}.")
        open_map_page(map_name)  # Refresh the map page to show the new macro

    # Open a new window for macro creation
    create_macro_win = Toplevel(tk)
    create_macro_win.title(f"Create Macro for {map_name.capitalize()}")
    create_macro_win.configure(bg="#bdeaff")

    # Label and entry for macro name
    (Label(create_macro_win, text="Enter Macro Name:", bg="#bdeaff", font=("New Amsterdam", 12))
     .grid(row=0, column=0, padx=10, pady=10))
    entry = Entry(create_macro_win, font=("New Amsterdam", 12))
    entry.grid(row=0, column=1, padx=10, pady=10)

    # Button to start recording
    Button(create_macro_win, text="Start Recording", bg='red', fg='white', font=("New Amsterdam", 12, 'bold'),
           command=start_recording).grid(row=1, column=0, columnspan=2, pady=10)


# Load macros from file
def load_macros(map_name, listbox):
    try:
        with open(f'macros/{map_name}_macros.json', 'r') as f:
            macros = json.load(f)
            for macro in macros:
                listbox.insert(END, macro)
    except FileNotFoundError:
        print('No macros yet for this map')
        pass


# Define a function to load and resize images
def load_and_resize_image(filename, size=(150, 100)):
    try:
        img = Image.open(filename)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image {filename}: {e}")
        return None


map_names = ['abyss', 'ascent', 'bind', 'breeze', 'fracture', 'haven', 'icebox', 'lotus', 'pearl', 'split', 'sunset']

# Store image references to prevent garbage collection
image_references = []

# Create a list of buttons
buttons = []

# Generate all the maps onto the main page
for i, map_name in enumerate(map_names):
    file_path = f"images/valorant_maps/{map_name}.png"
    new_img = load_and_resize_image(file_path)
    if new_img:  # Only create a button if the image was loaded successfully
        image_references.append(new_img)  # Keep a reference to the image
        button = Button(tk, image=new_img, text=map_name.capitalize(),
                        compound=CENTER,
                        font=("New Amsterdam", 12, 'bold'), fg='white', relief=FLAT,
                        command=lambda name=map_name: open_map_page(name))
        button.grid(row=2 + i // 3, column=i % 3, padx=5, pady=5)
        buttons.append(button)  # Keep a reference to the button to prevent garbage collection

        # TODO Add feature to delete a specific macro

tk.mainloop()
