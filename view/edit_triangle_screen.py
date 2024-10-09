import tkinter as tk
from tkinter import Entry, Button
from database import triangle
from view import consts
from service import edit_triangle as edit


def open_edit_triangle_window(root, triangle: triangle.Triangle, db: triangle.TriangleDatabase):
    """
    Opens a new window with editable fields for triangle's name and points.
    Other fields such as perimeter, area, type based on sides, and type based on angles are non-editable.
    """
    # Create a new window for editing
    edit_window = tk.Toplevel()
    edit_window.title(f"Edit Triangle: {triangle.name}")
    edit_window.geometry("300x400")

    # Name field
    name_label = tk.Label(edit_window, text="Triangle Name:")
    name_label.pack(pady=5)
    name_entry = Entry(edit_window, width=30)
    name_entry.pack(pady=5)
    name_entry.insert(0, triangle.name)  # Insert the current name

    points = triangle.points

    # Points fields (Editable - x1, y1, x2, y2, x3, y3 separately)
    points_label = tk.Label(edit_window, text="Points:")
    points_label.pack(pady=5)

    # Create a frame to hold the point entries in grid format
    points_frame = tk.Frame(edit_window)
    points_frame.pack(pady=5)

    # Labels and entry fields for x1, y1
    x1_label = tk.Label(points_frame, text="x1:")
    x1_label.grid(row=0, column=0, padx=5, pady=5)
    x1_entry = tk.Entry(points_frame, width=10)
    x1_entry.grid(row=0, column=1, padx=5, pady=5)
    x1_entry.insert(0, points[0][0])  # Insert x1 value

    y1_label = tk.Label(points_frame, text="y1:")
    y1_label.grid(row=0, column=2, padx=5, pady=5)
    y1_entry = tk.Entry(points_frame, width=10)
    y1_entry.grid(row=0, column=3, padx=5, pady=5)
    y1_entry.insert(0, points[0][1])  # Insert y1 value

    # Labels and entry fields for x2, y2
    x2_label = tk.Label(points_frame, text="x2:")
    x2_label.grid(row=1, column=0, padx=5, pady=5)
    x2_entry = tk.Entry(points_frame, width=10)
    x2_entry.grid(row=1, column=1, padx=5, pady=5)
    x2_entry.insert(0, points[1][0])  # Insert x2 value

    y2_label = tk.Label(points_frame, text="y2:")
    y2_label.grid(row=1, column=2, padx=5, pady=5)
    y2_entry = tk.Entry(points_frame, width=10)
    y2_entry.grid(row=1, column=3, padx=5, pady=5)
    y2_entry.insert(0, points[1][1])  # Insert y2 value

    # Labels and entry fields for x3, y3
    x3_label = tk.Label(points_frame, text="x3:")
    x3_label.grid(row=2, column=0, padx=5, pady=5)
    x3_entry = tk.Entry(points_frame, width=10)
    x3_entry.grid(row=2, column=1, padx=5, pady=5)
    x3_entry.insert(0, points[2][0])  # Insert x3 value

    y3_label = tk.Label(points_frame, text="y3:")
    y3_label.grid(row=2, column=2, padx=5, pady=5)
    y3_entry = tk.Entry(points_frame, width=10)
    y3_entry.grid(row=2, column=3, padx=5, pady=5)
    y3_entry.insert(0, points[2][1])  # Insert y3 value

    # Perimeter (Non-editable)
    perimeter_label = tk.Label(
        edit_window, text=f"Perimeter: {triangle.perimeter}")
    perimeter_label.pack(pady=5)

    # Area (Non-editable)
    area_label = tk.Label(edit_window, text=f"Area: {triangle.area}")
    area_label.pack(pady=5)

    # Type based on sides (Non-editable)
    type_sides_label = tk.Label(
        edit_window, text=f"Type (Sides): {triangle.type_based_on_sides}")
    type_sides_label.pack(pady=5)

    # Type based on angles (Non-editable)
    type_angles_label = tk.Label(
        edit_window, text=f"Type (Angles): {triangle.type_based_on_angles}")
    type_angles_label.pack(pady=5)

    # Validation result label
    validation_label = tk.Label(
        edit_window, text="", font=(consts.DEFAULT_SCREEN_FONT, 12))
    validation_label.pack(pady=5)

    # Submit button to save changes
    submit_button = Button(edit_window, text="Submit", command=lambda: edit.edit_triangle(root,
                                                                                          validation_label, triangle, db, name_entry, x1_entry, y1_entry, x2_entry, y2_entry, x3_entry, y3_entry))
    submit_button.pack(pady=10)
