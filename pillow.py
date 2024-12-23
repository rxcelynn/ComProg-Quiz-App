from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Test")

# Corrected file path
image = Image.open(r"C:\Users\Lenovo\OneDrive\Documents\Rocelyn - LV\comprog\project\blue.jpg")
photo = ImageTk.PhotoImage(image)

# Display the image in a Label
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()
