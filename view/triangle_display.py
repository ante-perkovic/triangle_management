import tkinter as tk


def create_triangle_window():
    # Create a new window for drawing the triangle
    triangle_window = tk.Toplevel()
    triangle_window.title("Triangle Drawing")
    triangle_window.geometry("500x600")

    return triangle_window


def display_triangle(canvas, triangle_points):

    # Extract triangle points
    x1 = triangle_points[0][0]
    y1 = triangle_points[0][1]
    x2 = triangle_points[1][0]
    y2 = triangle_points[1][1]
    x3 = triangle_points[2][0]
    y3 = triangle_points[2][1]

    # Render triangle on canvas
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='', outline='black')
