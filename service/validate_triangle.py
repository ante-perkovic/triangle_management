
from service import consts as service_consts
from service import calculate_triangle as calculation
import view.triangle_display as display
from view import consts as view_consts
import tkinter as tk


def validate_triangle_sides(validation_label, side1, side2, side3):
    try:
        # Get side lengths from the inputs
        side1 = float(side1)
        side2 = float(side2)
        side3 = float(side3)

        # Validation: Check if the sides form a valid triangle
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            validation_label.config(
                text="Invalid triangle: The sum of any two sides must be greater than the third side.", fg="red")
        elif side1 <= 0 or side2 <= 0 or side3 <= 0:
            validation_label.config(
                text="Invalid input: Sides must be positive.", fg="red")
        else:
            validation_label.config(
                text=service_consts.VALID_TRIANGLE_MESSAGE, fg="green")

            # Create a new window for drawing the triangle
            triangle_window = display.create_triangle_window()

            frame = tk.Frame(triangle_window)
            frame.pack(fill=tk.BOTH, expand=True)

            # Create a canvas in the frame
            canvas = tk.Canvas(frame, width=500, height=400, bg="white")
            canvas.pack(pady=10)  # Add some padding for visibility

            # Clear the canvas before drawing
            canvas.delete('all')

            # Calculate triangle points
            triangle_points = calculation.calculate_triangle_from_sides(
                view_consts.TRIANGLE_BASE_X, view_consts.TRIANGLE_BASE_Y, side1, side2, side3)
            display.display_triangle(canvas, triangle_points)

            # Add labels below the canvas
            area_label = tk.Label(
                frame, text=f"Area: {calculation.herons_area(side1, side2, side3)}")
            area_label.pack(pady=10)

            type_sides_label = tk.Label(
                frame, text=f"Type based on sides: {calculation.triangle_type_based_on_sides(side1, side2, side3)}")
            type_sides_label.pack(pady=5)

            type_angles_label = tk.Label(
                frame, text=f"Type based on angles: {calculation.triangle_type_based_on_angles(side1, side2, side3)}")
            type_angles_label.pack(pady=5)
    except ValueError:
        validation_label.config(
            text=service_consts.INVALID_NUMBERS_MESSAGE, fg="red")


def validate_triangle_angles(validation_label, angle1, angle2, angle3):
    try:
        # Get angles from the inputs
        angle1 = float(angle1)
        angle2 = float(angle2)
        angle3 = float(angle3)

        # Validation: The sum of the angles must be exactly 180 degrees
        if angle1 + angle2 + angle3 != 180:
            validation_label.config(
                text="Invalid triangle: The sum of angles must be exactly 180 degrees.", fg="red")
        elif angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
            validation_label.config(
                text="Invalid triangle: Angles must be positive.", fg="red")
        else:
            validation_label.config(
                text=service_consts.VALID_TRIANGLE_MESSAGE, fg="green")

            # Create a new window for drawing the triangle
            triangle_window = display.create_triangle_window()

            frame = tk.Frame(triangle_window)
            frame.pack(fill=tk.BOTH, expand=True)

            # Create a canvas in the frame
            canvas = tk.Canvas(frame, width=500, height=400, bg="white")
            canvas.pack(pady=10)  # Add some padding for visibility

            # Clear the canvas before drawing
            canvas.delete('all')

            # Calculate triangle points
            triangle_points = calculation.calculate_triangle_from_angles(
                view_consts.TRIANGLE_BASE_X, view_consts.TRIANGLE_BASE_Y, angle1, angle2, angle3)
            display.display_triangle(canvas, triangle_points)

            # Calculate triangle sides from points
            triangle_sides = calculation.triangle_points_to_sides(
                triangle_points)

            # Add labels below the canvas
            notice_label = tk.Label(
                frame, text="When provided with only angles, one side is size 200")
            notice_label.pack(pady=10)
            area_label = tk.Label(
                frame, text=f"Area: {calculation.trigonometric_area(angle1, angle2, angle3, 'angles')}")
            area_label.pack(pady=5)

            type_sides_label = tk.Label(
                frame, text=f"Type based on sides: {calculation.triangle_type_based_on_sides(triangle_sides[0], triangle_sides[1], triangle_sides[2])}")
            type_sides_label.pack(pady=5)

            type_angles_label = tk.Label(
                frame, text=f"Type based on angles: {calculation.triangle_type_based_on_angles(triangle_sides[0], triangle_sides[1], triangle_sides[2])}")
            type_angles_label.pack(pady=5)

    except ValueError:
        validation_label.config(
            text=service_consts.INVALID_NUMBERS_MESSAGE, fg="red")


def validate_sides_and_angle(validation_label, side1, side2, angle):
    try:
        # Get sides and angle
        side1 = float(side1)
        side2 = float(side2)
        angle = float(angle)

        # Simple validation: Check if sides are positive and angle is between 0 and 180
        if side1 <= 0 or side2 <= 0 or angle <= 0 or angle >= 180:
            validation_label.config(
                text="Invalid input: Sides must be positive, and angle must be between 0 and 180 degrees.", fg="red")
        else:
            validation_label.config(
                text=service_consts.VALID_TRIANGLE_MESSAGE, fg="green")

            # Create a new window for drawing the triangle
            triangle_window = display.create_triangle_window()

            frame = tk.Frame(triangle_window)
            frame.pack(fill=tk.BOTH, expand=True)

            # Create a canvas in the frame
            canvas = tk.Canvas(frame, width=500, height=400, bg="white")
            canvas.pack(pady=10)  # Add some padding for visibility

            # Clear the canvas before drawing
            canvas.delete('all')

            # Calculate triangle points
            triangle_points = calculation.calculate_triangle_from_sides_and_angle(
                view_consts.TRIANGLE_BASE_X, view_consts.TRIANGLE_BASE_Y, side1, side2, angle)
            display.display_triangle(canvas, triangle_points)

            # Calculate triangle sides from points
            triangle_sides = calculation.triangle_points_to_sides(
                triangle_points)

            # Add labels below the canvas
            area_label = tk.Label(
                frame, text=f"Area: {calculation.trigonometric_area(side1, side2, angle, 'sides and angle')}")
            area_label.pack(pady=5)

            type_sides_label = tk.Label(
                frame, text=f"Type based on sides: {calculation.triangle_type_based_on_sides(triangle_sides[0], triangle_sides[1], triangle_sides[2])}")
            type_sides_label.pack(pady=5)

            type_angles_label = tk.Label(
                frame, text=f"Type based on angles: {calculation.triangle_type_based_on_angles(triangle_sides[0], triangle_sides[1], triangle_sides[2])}")
            type_angles_label.pack(pady=5)

    except ValueError:
        validation_label.config(
            text=service_consts.INVALID_NUMBERS_MESSAGE, fg="red")
