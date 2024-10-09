def validate_triangle_sides(side1, side2, side3):
    # Validation: Check if the sides form a valid triangle
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Invalid input: Sides must be positive."
    elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "Invalid triangle: The sum of any two sides must be greater than the third side."
    else:
        return None


def validate_triangle_angles(angle1, angle2, angle3):
    # Validation: The sum of the angles must be exactly 180 degrees, and angles must be between 0 and 180
    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0 or angle1 >= 180 or angle2 >= 180 or angle2 >= 180:
        return "Invalid triangle: Angles must be between 0 and 180 degrees."
    elif angle1 + angle2 + angle3 != 180:
        return "Invalid triangle: The sum of angles must be exactly 180 degrees."
    else:
        return None


def validate_triangle_sides_and_angle(side1, side2, angle):
    # Simple validation: Check if sides are positive and angle is between 0 and 180
    if side1 <= 0 or side2 <= 0:
        return "Invalid input: Sides must be positive and bigger than 0."
    if angle <= 0 or angle >= 180:
        return "Invalid input: Angle must be between 0 and 180 degrees."
    else:
        return None
