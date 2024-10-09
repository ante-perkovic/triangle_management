import math
from service import consts
from database import triangle


def triangle_points_to_sides(triangle_points):
    # Unpack the points
    (x1, y1), (x2, y2), (x3, y3) = triangle_points

    # Calculate the lengths of the sides using the distance formula
    # Side between points 1 and 2
    side1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # Side between points 2 and 3
    side2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    # Side between points 1 and 3
    side3 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    return side1, side2, side3

# Calculate perimeter of the triangle


def perimeter(side1, side2, side3):
    return side1 + side2 + side3

# Calculate area size of triagle using Heron's formula


def herons_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2  # Semi-perimeter

    # Area formula
    return round(math.sqrt(s * (s - side1) * (s - side2) * (s - side3)), 2)

# Calculate area size of triagle using trigonometry


def trigonometric_area(a, b, c, input):
    if input == "angles":
        side1 = consts.DEFAULT_SIDE_SIZE
        side2 = (math.sin(math.radians(b)) /
                 math.sin(math.radians(a))) * side1

    else:
        side1 = a
        side2 = b

    return round(0.5 * side1 * side2 * math.sin(math.radians(c)), 2)

# Calculates points of triangle using sides


def calculate_triangle_from_sides(base_x, base_y, side1, side2, side3):
    # Calculate the area using Heron's formula
    area = herons_area(side1, side2, side3)

    # Calculate height from the area
    height = (2 * area) / side3

    # Vertices of the triangle (assuming base is along the x-axis)
    x1, y1 = base_x, base_y
    x2, y2 = base_x + side3, base_y  # Second vertex at (side3, 0)

    # Calculate the third vertex (x3, y3) using Pythagorean theorem
    x3 = base_x + (side2**2 - height**2)**0.5
    y3 = base_y - height

    return [[x1, y1], [x2, y2], [x3, y3]]

# Calculates points of triangle using sides and angle


def calculate_triangle_from_sides_and_angle(base_x, base_y, side1, side2, angle):
    # Vertex 1 is at the origin (base_x, base_y)
    x1, y1 = base_x, base_y

    # Vertex 2 is along the x-axis (side 'side2')
    x2, y2 = base_x + side2, base_y

    # Calculate vertex 3 using trigonometry (side 'side1' and angle angle3)
    x3 = base_x + side1 * math.cos(math.radians(angle))
    y3 = base_y - side1 * math.sin(math.radians(angle))

    return [[x1, y1], [x2, y2], [x3, y3]]

# Calculates points of triangle using angles


def calculate_triangle_from_angles(base_x, base_y, angle1, angle2, angle3):
    # Assume side1 unit triangle with sides side1, side2, side3 and angle angle1, angle2, angle3
    # Assume side 'side3' = 200 for visualization purposes
    side3 = consts.DEFAULT_SIDE_SIZE
    side2 = side3 * math.sin(math.radians(angle2)) / \
        math.sin(math.radians(angle3))
    side1 = side3 * math.sin(math.radians(angle1)) / \
        math.sin(math.radians(angle3))

    # Vertex 1 is at the origin (base_x, base_y)
    x1, y1 = base_x, base_y

    # Vertex 2 is along the x-axis (side 'side3')
    x2, y2 = base_x + side3, base_y

    # Calculate vertex 3 using trigonometry
    x3 = base_x + side2 * math.cos(math.radians(angle1))
    y3 = base_y - side2 * math.sin(math.radians(angle1))

    return [[x1, y1], [x2, y2], [x3, y3]]

# Define triangle type based on sides


def triangle_type_based_on_sides(side1, side2, side3):
    # Determine the type of triangle based on side lengths
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side2 == side3 or side3 == side1:
        return "Isosceles"
    else:
        return "Scalene"

# Define triangle type based on angles


def triangle_type_based_on_angles(side1, side2, side3):
    # Calculate the squares of the sides
    a2 = side1 ** 2
    b2 = side2 ** 2
    c2 = side3 ** 2

    # Sort the squares to simplify comparisons
    squares = sorted([a2, b2, c2])

    # Use the largest side's square to determine the angle types
    if squares[0] + squares[1] > squares[2]:
        return "Acute"  # All angles are less than 90°
    elif squares[0] + squares[1] == squares[2]:
        return "Right"  # One angle is exactly 90°
    else:
        return "Obtuse"  # One angle is greater than 90°

# Calculate triangle data using sides, returns Triangle object


def calculate_triangle_data(name, triangle_points, triangle_sides):
    perimeter_size = perimeter(
        triangle_sides[0], triangle_sides[1], triangle_sides[2])
    area_size = herons_area(
        triangle_sides[0], triangle_sides[1], triangle_sides[2])
    type_based_on_sides = triangle_type_based_on_sides(
        triangle_sides[0], triangle_sides[1], triangle_sides[2])
    type_based_on_angles = triangle_type_based_on_angles(
        triangle_sides[0], triangle_sides[1], triangle_sides[2])

    return triangle.Triangle(id=None,
                             name=name, points=triangle_points, perimeter=perimeter_size, area=area_size, type_based_on_sides=type_based_on_sides, type_based_on_angles=type_based_on_angles)
