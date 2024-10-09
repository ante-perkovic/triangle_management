
import tkinter as tk
from service import consts as service_consts
from service import calculate_triangle as calculation
from service import validate_triangle as validation
import view.triangle_display as display
from view import consts as view_consts
from database import triangle


def create_triangle_from_sides(validation_label, name, side1, side2, side3, db: triangle.TriangleDatabase):
    try:
        # Get side lengths from the inputs
        side1 = float(side1)
        side2 = float(side2)
        side3 = float(side3)

    except ValueError:
        # Display message for invalid input numbers
        validation_label.config(
            text=service_consts.INVALID_NUMBERS_MESSAGE, fg="red")

    # Validate triangle sides
    err = validation.validate_triangle_sides(side1, side2, side3)
    if err:
        # Display error message
        validation_label.config(
            text=err, fg="red")
        return
    else:
        # Display valid triangle message
        validation_label.config(
            text=service_consts.VALID_TRIANGLE_MESSAGE, fg="green")

    # Calculate triangle points
    triangle_points = calculation.calculate_triangle_from_sides(
        view_consts.TRIANGLE_BASE_X, view_consts.TRIANGLE_BASE_Y, side1, side2, side3)

    # Calculate all triangle data from sides
    triangle_model = calculation.calculate_triangle_data(
        name, triangle_points, [side1, side2, side3])

    # Add triangle to database
    err = db.add_triangle(triangle_model)
    if err:
        # Display error message if adding to database fails
        validation_label.config(
            text=err, fg="red")
        return

    # Create a new window and frame for drawing the triangle
    triangle_window = display.create_triangle_window()

    frame = tk.Frame(triangle_window)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas in the frame
    canvas = tk.Canvas(frame, width=500, height=400, bg="white")
    canvas.pack(pady=10)  # Add some padding for visibility

    # Clear the canvas before drawing
    canvas.delete('all')

    # Visualise triangle on canvas
    display.display_triangle(canvas, triangle_points)

    # Add labels below the canvas
    perimeter_label = tk.Label(
        frame, text=f"Area: {triangle_model.perimeter}")
    perimeter_label.pack(pady=10)
    area_label = tk.Label(
        frame, text=f"Area: {triangle_model.area}")
    area_label.pack(pady=5)

    type_sides_label = tk.Label(
        frame, text=f"Type based on sides: {triangle_model.type_based_on_sides}")
    type_sides_label.pack(pady=5)

    type_angles_label = tk.Label(
        frame, text=f"Type based on angles: {triangle_model.type_based_on_angles}")
    type_angles_label.pack(pady=5)


def create_triangle_from_angles(validation_label, name, angle1, angle2, angle3, db: triangle.TriangleDatabase):
    try:
        # Get angles from the inputs
        angle1 = float(angle1)
        angle2 = float(angle2)
        angle3 = float(angle3)

    except ValueError:
        # Display message for invalid input numbers
        validation_label.config(
            text=service_consts.INVALID_NUMBERS_MESSAGE, fg="red")

    # Validate triangle angles
    err = validation.validate_triangle_angles(angle1, angle2, angle3)
    if err:
        # Display error message if validation fails
        validation_label.config(
            text=err, fg="red")
        return
    else:
        # Display valid triangle message
        validation_label.config(
            text=service_consts.VALID_TRIANGLE_MESSAGE, fg="green")

    # Calculate triangle points
    triangle_points = calculation.calculate_triangle_from_angles(
        view_consts.TRIANGLE_BASE_X, view_consts.TRIANGLE_BASE_Y, angle1, angle2, angle3)

    # Calculate triangle sides from points
    triangle_sides = calculation.triangle_points_to_sides(
        triangle_points)

    # Calculate all triangle data from sides
    triangle_model = calculation.calculate_triangle_data(
        name, triangle_points, triangle_sides)

    # Add triangle to database
    err = db.add_triangle(triangle_model)
    if err:
        # Display error message
        validation_label.config(
            text=err, fg="red")
        return

    # Create a new window and frame for drawing the triangle
    triangle_window = display.create_triangle_window()

    frame = tk.Frame(triangle_window)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas in the frame
    canvas = tk.Canvas(frame, width=500, height=400, bg="white")
    canvas.pack(pady=10)  # Add some padding for visibility

    # Clear the canvas before drawing
    canvas.delete('all')

    # Visualise triangle on canvas
    display.display_triangle(canvas, triangle_points)

    # Add labels below the canvas
    notice_label = tk.Label(
        frame, text="When provided with only angles, one side is size 200")
    notice_label.pack(pady=10)
    perimeter_label = tk.Label(
        frame, text=f"Area: {triangle_model.perimeter}")
    perimeter_label.pack(pady=10)
    area_label = tk.Label(
        frame, text=f"Area: {triangle_model.area}")
    area_label.pack(pady=5)

    type_sides_label = tk.Label(
        frame, text=f"Type based on sides: {triangle_model.type_based_on_sides}")
    type_sides_label.pack(pady=5)

    type_angles_label = tk.Label(
        frame, text=f"Type based on angles: {triangle_model.type_based_on_angles}")
    type_angles_label.pack(pady=5)


def create_triangle_from_sides_and_angles(validation_label, name, side1, side2, angle, db: triangle.TriangleDatabase):
    try:
        # Get sides and angle
        side1 = float(side1)
        side2 = float(side2)
        angle = float(angle)

    except ValueError:
        # Display message for invalid input numbers
        validation_label.config(
            text=service_consts.INVALID_NUMBERS_MESSAGE, fg="red")

    # Validate triangle sides and angle
    err = validation.validate_triangle_sides_and_angle(side1, side2, angle)
    if err:
        # Display error message
        validation_label.config(
            text=err, fg="red")
        return
    else:
        # Display valid triangle message
        validation_label.config(
            text=service_consts.VALID_TRIANGLE_MESSAGE, fg="green")

    # Calculate triangle points
    triangle_points = calculation.calculate_triangle_from_sides_and_angle(
        view_consts.TRIANGLE_BASE_X, view_consts.TRIANGLE_BASE_Y, side1, side2, angle)

    # Calculate triangle sides from points
    triangle_sides = calculation.triangle_points_to_sides(
        triangle_points)

    # Calculate all triangle data from sides
    triangle_model = calculation.calculate_triangle_data(
        name, triangle_points, triangle_sides)

    # Add triangle to database
    err = db.add_triangle(triangle_model)
    if err:
        # Display error message
        validation_label.config(
            text=err, fg="red")
        return

    # Create a new window for drawing the triangle
    triangle_window = display.create_triangle_window()

    frame = tk.Frame(triangle_window)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas in the frame
    canvas = tk.Canvas(frame, width=500, height=400, bg="white")
    canvas.pack(pady=10)  # Add some padding for visibility

    # Clear the canvas before drawing
    canvas.delete('all')

    # Visualise triangle on canvas
    display.display_triangle(canvas, triangle_points)

    # Add labels below the canvas
    notice_label = tk.Label(
        frame, text="When provided with only angles, one side is size 200")
    notice_label.pack(pady=10)
    perimeter_label = tk.Label(
        frame, text=f"Area: {triangle_model.perimeter}")
    perimeter_label.pack(pady=10)
    area_label = tk.Label(
        frame, text=f"Area: {triangle_model.area}")
    area_label.pack(pady=5)

    type_sides_label = tk.Label(
        frame, text=f"Type based on sides: {triangle_model.type_based_on_sides}")
    type_sides_label.pack(pady=5)

    type_angles_label = tk.Label(
        frame, text=f"Type based on angles: {triangle_model.type_based_on_angles}")
    type_angles_label.pack(pady=5)
