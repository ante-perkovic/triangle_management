# Function to clear all widgets from the window
def clear_frame(root):
    for widget in root.winfo_children():
        widget.destroy()