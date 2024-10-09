
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
            triangle_window = tk.Toplevel()
            triangle_window.title("Triangle Drawing")
            triangle_window.geometry("500x400")

            # Create a canvas in the new window
            canvas = tk.Canvas(triangle_window, width=500, height=400)
            canvas.pack()

            # Clear the canvas before drawing
            canvas.delete('all')

            triangle_points = calculation.calculate_triangle_from_sides(
                view_consts.TRIANGLE_BASE_X, view_consts.TRIANGLE_BASE_Y, side1, side2, side3)
            display.display_triangle(canvas, triangle_points)
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
    except ValueError:
        validation_label.config(
            text=service_consts.INVALID_NUMBERS_MESSAGE, fg="red")
