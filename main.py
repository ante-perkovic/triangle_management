import tkinter as tk
import view.selection_screen as selection

# Create the main window
root = tk.Tk()
root.minsize(600, 300)
root.title("Triangle Manager")

# Show the main selection screen initially
selection.show_selection_screen(root)

# Start the tkinter main loop
root.mainloop()
