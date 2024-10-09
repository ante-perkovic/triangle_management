import tkinter as tk
import view.main_screen as main_screen
from database import triangle

# Initiate database
db = triangle.TriangleDatabase()

# Create the main window
root = tk.Tk()
root.minsize(600, 300)
root.title("Triangle Manager")

# On closing of tkinter close database


def on_closing():
    db.close()
    root.destroy()  # Close the Tkinter window


# Show main screen
main_screen.show_main_screen(root, db)

# Bind the closing event of the window to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the tkinter main loop
root.mainloop()
