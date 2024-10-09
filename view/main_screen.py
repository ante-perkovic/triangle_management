import tkinter as tk
import view.selection_screen as selection
import view.list_triangles as triangles
import view.helper as helper


def show_main_screen(root, db):
    # Clear frame before rendering screen
    helper.clear_frame(root)

    # Create a frame for the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=50)  # Add some vertical padding

    # Create "Create new triangle" button
    new_triangle_button = tk.Button(
        button_frame, text="Create New Triangle", command=lambda: selection.show_selection_screen(root, db))
    new_triangle_button.pack(pady=10)   # Add some vertical padding

    # Create "Stored Triangles" button
    stored_triangles_button = tk.Button(
        button_frame, text="Stored Triangles", command=lambda: triangles.show_listed_triangles_screen(root, db))
    stored_triangles_button.pack(pady=10)   # Add some vertical padding
