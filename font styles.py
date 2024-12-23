import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Font Styling Example")

# Example Label with Bold Font
label_bold = tk.Label(root, text="This is Bold Text", font=("Arial", 14, "bold"))
label_bold.pack(pady=10)

# Example Label with Italic Font
label_italic = tk.Label(root, text="This is Italic Text", font=("Verdana", 12, "italic"))
label_italic.pack(pady=10)

# Example Label with Underlined Font
label_underline = tk.Label(root, text="This is Underlined Text", font=("Courier New", 14, "underline"))
label_underline.pack(pady=10)

# Example ttk.Label with Custom Font
style = ttk.Style()
style.configure("Custom.TLabel", font=("Times New Roman", 14, "bold italic"))
label_custom = ttk.Label(root, text="This is Bold + Italic Text", style="Custom.TLabel")
label_custom.pack(pady=10)

root.mainloop()
