import tkinter as tk
from tkinter import messagebox, Frame, Entry, Button
from database import triangle as triangleObject
import view.helper as helper
import view.main_screen as main_screen
import view.triangle_display as display
import view.edit_triangle_screen as edit


def show_listed_triangles_screen(root, db):
    # Clear frame before rendering screen
    helper.clear_frame(root)

    # Create a frame for the search bar and button
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)

    # Create the search entry
    search_entry = Entry(search_frame, width=30)
    search_entry.pack(side=tk.LEFT, padx=5)

    # Create the search button
    search_button = Button(search_frame, text="Search", command=lambda: display_triangles(root,
                                                                                          search_entry.get(), db, list_frame))
    search_button.pack(side=tk.LEFT)

    # Create a frame for the listbox and scrollbar
    list_frame = Frame(root)
    list_frame.pack(pady=10)

    # Display all triangles initially
    display_triangles(root, '', db, list_frame)

    # Back button to go back to the main root screen
    back_button = tk.Button(root, text="Back", width=40,
                            command=lambda: main_screen.show_main_screen(root, db))
    back_button.pack(pady=20)


def display_triangles(root, search_name, db, triangle_frame):
    # Clear the current list in the triangle_frame
    for widget in triangle_frame.winfo_children():
        widget.destroy()

    # Fetch triangles from the database
    if search_name:  # If there's a search term, use it
        triangles_db = db.cursor.execute(
            'SELECT * FROM triangles WHERE name LIKE ?', (search_name + '%',)).fetchall()
        triangles = [triangleObject.Triangle.from_db_row(
            triangle_db) for triangle_db in triangles_db]
    else:  # No search term, fetch all triangles
        triangles = db.fetch_triangles()

    # Display triangles in the triangle_frame
    for triangle in triangles:
        row_frame = Frame(triangle_frame)
        row_frame.pack(fill=tk.X, padx=10, pady=5)

        # Triangle name label
        triangle_label = tk.Label(
            row_frame, text=f"Id: {triangle.id}; Triangle name: {triangle.name}", width=30, anchor='w')
        triangle_label.pack(side=tk.LEFT, padx=5)

        # View button
        view_button = tk.Button(row_frame, text="View",
                                command=lambda t=triangle: view_triangle(t))
        view_button.pack(side=tk.LEFT, padx=5)

        # Edit button
        edit_button = tk.Button(row_frame, text="Edit",
                                command=lambda t=triangle: edit_triangle(root, t, db))
        edit_button.pack(side=tk.LEFT, padx=5)

        # Delete button
        delete_button = tk.Button(
            row_frame, text="Delete", command=lambda t=triangle: delete_triangle(root, t.name, db, triangle_frame))
        delete_button.pack(side=tk.LEFT, padx=5)

    # Check if no triangles were found
    if not triangles:
        messagebox.showinfo(
            "No Results", "No triangles found matching your search.")


def view_triangle(triangle):
    # Create a new window for drawing the triangle
    triangle_window = display.create_triangle_window()

    frame = tk.Frame(triangle_window)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas in the frame
    canvas = tk.Canvas(frame, width=500, height=400, bg="white")
    canvas.pack(pady=10)  # Add some padding for visibility

    # Clear the canvas before drawing
    canvas.delete('all')

    # Display the triangle on the canvas
    display.display_triangle(canvas, triangle.points)

    # Optionally, display other details about the triangle
    details_label = tk.Label(triangle_window, text=f"Name: {triangle.name}\n"
                                                   f"Perimeter: {triangle.perimeter}\n"
                                                   f"Area: {triangle.area}\n"
                                                   f"Type (Sides): {triangle.type_based_on_sides}\n"
                                                   f"Type (Angles): {triangle.type_based_on_angles}")
    details_label.pack(pady=10)


def edit_triangle(root, triangle, db):
    edit.open_edit_triangle_window(root, triangle, db)


def delete_triangle(root, triangle_name, db, triangle_frame):
    # Delete the triangle from the database
    db.cursor.execute('DELETE FROM triangles WHERE name = ?', (triangle_name,))
    db.connection.commit()

    # Refresh the list after deletion
    display_triangles(root, '', db, triangle_frame)
