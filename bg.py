import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Import from Pillow

# Create the main application window
root = tk.Tk()
root.title("TESTINGGG AAAAAAAAA")
root.geometry("500x400")

# Load the JPEG image
background_image = Image.open(r"pink.jpg")  # Replace with your .jpg file
background_photo = ImageTk.PhotoImage(background_image)

# Create a Canvas to display the background
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)

# Place the image on the canvas
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Add widgets on top of the image
label = ttk.Label(root, text="Welcome sa PINK kong odnum!", font=("Arial", 14, "bold"))
canvas.create_window(250, 100, window=label)

button = ttk.Button(root, text="pindot dito, boss", command=lambda: print("Button clicked!"))
canvas.create_window(250, 200, window=button)

root.mainloop()
