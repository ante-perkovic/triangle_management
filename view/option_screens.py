import tkinter as tk
import view.helper as helper
import view.consts as consts
import view.selection_screen as selection
from service import validate_triangle as validation

# Function to switch to the option screen (3 input fields for sides)


def show_option1_screen(root):
    helper.clear_frame(root)

    # Side length inputs and labels
    side1_label = tk.Label(root, text="Side 1:")
    side1_label.pack(pady=5)
    side1_entry = tk.Entry(root)
    side1_entry.pack(pady=5)

    side2_label = tk.Label(root, text="Side 2:")
    side2_label.pack(pady=5)
    side2_entry = tk.Entry(root)
    side2_entry.pack(pady=5)

    side3_label = tk.Label(root, text="Side 3:")
    side3_label.pack(pady=5)
    side3_entry = tk.Entry(root)
    side3_entry.pack(pady=5)

    # Validation result label
    validation_label = tk.Label(
        root, text="", font=(consts.DEFAULT_SCREEN_FONT, 12))
    validation_label.pack(pady=5)

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=lambda: validation.validate_triangle_sides(
        validation_label, side1_entry.get(), side2_entry.get(), side3_entry.get()))
    submit_button.pack(pady=10)

    # Back button
    back_button = tk.Button(
        root, text="Back", command=lambda: selection.show_selection_screen(root))
    back_button.pack(pady=10)

# Function to switch to the option screen (3 inputs for angles)


def show_option2_screen(root):
    helper.clear_frame(root)

    # Angle inputs and labels
    angle1_label = tk.Label(root, text="Angle 1:")
    angle1_label.pack(pady=5)
    angle1_entry = tk.Entry(root)
    angle1_entry.pack(pady=5)

    angle2_label = tk.Label(root, text="Angle 2:")
    angle2_label.pack(pady=5)
    angle2_entry = tk.Entry(root)
    angle2_entry.pack(pady=5)

    angle3_label = tk.Label(root, text="Angle 3:")
    angle3_label.pack(pady=5)
    angle3_entry = tk.Entry(root)
    angle3_entry.pack(pady=5)

    # Validation result label
    validation_label = tk.Label(
        root, text="", font=(consts.DEFAULT_SCREEN_FONT, 12))
    validation_label.pack(pady=5)

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=lambda: validation.validate_triangle_angles(
        validation_label, angle1_entry.get(), angle2_entry.get(), angle3_entry.get()))
    submit_button.pack(pady=10)

    # Back button
    back_button = tk.Button(
        root, text="Back", command=lambda: selection.show_selection_screen(root))
    back_button.pack(pady=10)

# Function to switch to the option screen (2 side lengths and 1 angle)


def show_option3_screen(root):
    helper.clear_frame(root)

    # Side length inputs and labels
    side1_label = tk.Label(root, text="Side 1:")
    side1_label.pack(pady=5)
    side1_entry = tk.Entry(root)
    side1_entry.pack(pady=5)

    side2_label = tk.Label(root, text="Side 2:")
    side2_label.pack(pady=5)
    side2_entry = tk.Entry(root)
    side2_entry.pack(pady=5)

    angle_label = tk.Label(root, text="Angle (between sides):")
    angle_label.pack(pady=5)
    angle_entry = tk.Entry(root)
    angle_entry.pack(pady=5)

    # Validation result label
    validation_label = tk.Label(
        root, text="", font=(consts.DEFAULT_SCREEN_FONT, 12))
    validation_label.pack(pady=5)

    # Submit button
    submit_button = tk.Button(
        root, text="Submit", command=lambda: validation.validate_sides_and_angle(validation_label, side1_entry.get(), side2_entry.get(), angle_entry.get()))
    submit_button.pack(pady=10)

    # Back button
    back_button = tk.Button(
        root, text="Back", command=lambda: selection.show_selection_screen(root))
    back_button.pack(pady=10)
