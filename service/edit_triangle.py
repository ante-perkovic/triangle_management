from database import triangle
from service import consts as service_consts
from service import calculate_triangle as calculation
from service import validate_triangle as validation
from view import helper
from view import list_triangles as list_triangles


def edit_triangle(root, validation_label, triangle: triangle.Triangle, db: triangle.TriangleDatabase, name_entry, x1_entry, y1_entry, x2_entry, y2_entry, x3_entry, y3_entry):
    # Fetch new values
    triangle.name = name_entry.get()
    triangle.points[0][0] = x1_entry.get()
    triangle.points[0][1] = y1_entry.get()
    triangle.points[1][0] = x2_entry.get()
    triangle.points[1][1] = y2_entry.get()
    triangle.points[2][0] = x3_entry.get()
    triangle.points[2][1] = y3_entry.get()

    try:
        # Get angles from the inputs
        for point in triangle.points:
            point[0] = float(point[0])
            point[1] = float(point[1])

    except ValueError:
        # Display message for invalid input numbers
        validation_label.config(
            text=service_consts.INVALID_NUMBERS_MESSAGE, fg="red")

    # Calculate sides from triangle points
    triangle_sides = calculation.triangle_points_to_sides(
        triangle.points)

    # Validate triangle sides
    err = validation.validate_triangle_sides(
        triangle_sides[0], triangle_sides[1], triangle_sides[2])
    if err:
        # Display error message
        validation_label.config(
            text=err, fg="red")
        return
    else:
        # Display valid triangle message
        validation_label.config(
            text=service_consts.VALID_TRIANGLE_MESSAGE, fg="green")

    perimeter = calculation.perimeter(
        triangle_sides[0], triangle_sides[1], triangle_sides[2])
    area = calculation.herons_area(
        triangle_sides[0], triangle_sides[1], triangle_sides[2])
    type_based_on_sides = calculation.triangle_type_based_on_sides(
        triangle_sides[0], triangle_sides[1], triangle_sides[2])
    type_based_on_angles = calculation.triangle_type_based_on_angles(
        triangle_sides[0], triangle_sides[1], triangle_sides[2])

    # Assign calculated triangle data to Triangle object
    triangle.perimeter = perimeter
    triangle.area = area
    triangle.type_based_on_sides = type_based_on_sides
    triangle.type_based_on_angles = type_based_on_angles

    # Update triangle
    err = db.update_triangle(triangle.id, triangle)
    if err:
        # Display error message if update fails
        validation_label.config(
            text=err, fg="red")
        return
    else:
        # Display valid triangle message
        validation_label.config(
            text=service_consts.VALID_TRIANGLE_MESSAGE, fg="green")
    # Clear frame before rendering screen
    helper.clear_frame(root)  # Clear root window
    # Show updated triangle list
    list_triangles.show_listed_triangles_screen(
        root, db)
