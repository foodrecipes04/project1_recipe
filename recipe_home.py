import tkinter as tk
from tkinter import ttk

def open_enter_recipe():
    # Function to open the "Enter Your Recipe" page
    # You can replace this function with the code for the "Enter Your Recipe" page
    new_window = tk.Toplevel(root)
    new_window.title("Enter Your Recipe")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="You have selected: Enter Your Recipe")
    label.pack()

def open_search_recipe():
    # Function to open the "Search for Recipe" page
    # You can replace this function with the code for the "Search for Recipe" page
    new_window = tk.Toplevel(root)
    new_window.title("Search for Recipe")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="You have selected: Search for Recipe")
    label.pack()

root = tk.Tk()
root.title("Recipes")

# Add the heading "WORLD OF RECIPES" before the notebook
heading_label = tk.Label(root, text="WORLD OF RECIPES", font=("Arial", 20))
heading_label.pack(pady=10)

# Create a notebook (tab) widget
notebook = ttk.Notebook(root)

# Create two frames for the two options
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

# Add the frames to the notebook with respective tab names
notebook.add(frame1, text="Enter Your Recipe")
notebook.add(frame2, text="Search for Recipe")

notebook.pack(pady=10)

# Add content to the frames
# Option 1 content
option1_label = tk.Label(frame1, text="Welcome to Enter Your Recipe")
option1_label.pack(pady=20)
option1_button = tk.Button(frame1, text="Select Enter Your Recipe", command=open_enter_recipe)
option1_button.pack()

# Option 2 content
option2_label = tk.Label(frame2, text="Welcome to Search for Recipe")
option2_label.pack(pady=20)
option2_button = tk.Button(frame2, text="Select Search for Recipe", command=open_search_recipe)
option2_button.pack()

root.mainloop()