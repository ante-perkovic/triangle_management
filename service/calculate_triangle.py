import math


def herons_area(a, b, c):
    s = (a + b + c) / 2  # Semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Area formula
    return area


def calculate_triangle_from_sides(base_x, base_y, a, b, c):
    # Calculate the area using Heron's formula
    area = herons_area(a, b, c)

    # Calculate height from the area
    height = (2 * area) / c

    # Vertices of the triangle (assuming base is along the x-axis)
    x1, y1 = base_x, base_y
    x2, y2 = base_x + c, base_y  # Second vertex at (c, 0)

    # Calculate the third vertex (x3, y3) using Pythagorean theorem
    x3 = base_x + (b**2 - height**2)**0.5
    y3 = base_y - height

    return [[x1, y1], [x2, y2], [x3, y3]]


def calculate_triangle_from_sides_and_angle(base_x, base_y, a, b, C):
    # Vertex 1 is at the origin (base_x, base_y)
    x1, y1 = base_x, base_y

    # Vertex 2 is along the x-axis (side 'b')
    x2, y2 = base_x + b, base_y

    # Calculate vertex 3 using trigonometry (side 'a' and angle C)
    x3 = base_x + a * math.cos(C)
    y3 = base_y - a * math.sin(C)

    return [[x1, y1], [x2, y2], [x3, y3]]


def calculate_triangle_from_angles(base_x, base_y, A, B, C):
    # Assume a unit triangle with sides a, b, c and angle A, B, C
    # Assume side 'c' = 200 for visualization purposes
    c = 200
    b = c * math.sin(B) / math.sin(C)
    a = c * math.sin(A) / math.sin(C)

    # Vertex 1 is at the origin (base_x, base_y)
    x1, y1 = base_x, base_y

    # Vertex 2 is along the x-axis (side 'c')
    x2, y2 = base_x + c, base_y

    # Calculate vertex 3 using trigonometry
    x3 = base_x + b * math.cos(A)
    y3 = base_y - b * math.sin(A)

    return [[x1, y1], [x2, y2], [x3, y3]]
