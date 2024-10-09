import sqlite3
import ast  # Used to safely convert string representation back to a list of tuples
from service import calculate_triangle as calculation
# Define the SQLite database model for Triangle


class Triangle:
    def __init__(self, id, name, points, perimeter, area, type_based_on_sides, type_based_on_angles):
        self.id = id
        self.name = name
        # This will be a list of tuples [(x1, y1), (x2, y2), (x3, y3)]
        self.points = points
        self.perimeter = perimeter
        self.area = area
        self.type_based_on_sides = type_based_on_sides
        self.type_based_on_angles = type_based_on_angles

    def __repr__(self):
        return (f"Triangle(Name: {self.name}, Points: {self.points}, "
                f"Perimeter: {self.perimeter}, Area: {self.area}, "
                f"Type (Sides): {self.type_based_on_sides}, Type (Angles): {self.type_based_on_angles})")

    # Converts the Triangle object into a tuple suitable for database insertion.
    # The 'points' list of tuples will be converted into a string for storage.
    def to_db_tuple(self):
        points_str = str(self.points)  # Convert list of tuples to string
        return (self.name, points_str, self.perimeter, self.area, self.type_based_on_sides, self.type_based_on_angles)

    # Converts a database row into a Triangle object.
    # The 'points' string will be converted back into a list of tuples.
    @staticmethod
    def from_db_row(row):
        points = ast.literal_eval(
            row[2])  # Convert string back to list of tuples
        return Triangle(
            id=row[0],
            name=row[1],
            points=points,
            perimeter=row[3],
            area=row[4],
            type_based_on_sides=row[5],
            type_based_on_angles=row[6]
        )

# Define the SQLite database


class TriangleDatabase:
    def __init__(self, db_name='triangles.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    # Create the triangles table if it doesn't exist
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS triangles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                points TEXT NOT NULL UNIQUE,  -- We will store points as a string
                perimeter REAL NOT NULL,
                area REAL NOT NULL,
                type_based_on_sides TEXT NOT NULL,
                type_based_on_angles TEXT NOT NULL
            )
        ''')
        self.connection.commit()
    # Sort points to handle order differences.
    # Points is expected to be a list of tuples.
    # This function returns the points sorted by their coordinates, as a string.

    def _sort_points(self, points):
        sorted_points = sorted(points)
        return str(sorted_points)  # Convert sorted list of tuples to string

    # Adds a new triangle to the database.
    # Points are provided as a list of tuples [(x1, y1), (x2, y2), (x3, y3)].
    # Before adding, check for duplicates by sorted points and name.
    def add_triangle(self, triangle: Triangle):
        sorted_points = self._sort_points(triangle.points)
        existing_triangle = self.fetch_triangle_by_points(sorted_points)

        if existing_triangle:
            err = "Triangle with the same points already exists in the database."
            return err

        existing_triangle_by_name = self.fetch_triangle_by_name(triangle.name)
        if existing_triangle_by_name:
            err = "Triangle with the same name already exists in the database."
            return err

        # Insert a new triangle record into the database
        self.cursor.execute('''
            INSERT INTO triangles (name, points, perimeter, area, type_based_on_sides, type_based_on_angles)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (triangle.name, sorted_points, triangle.perimeter, triangle.area, triangle.type_based_on_sides, triangle.type_based_on_angles))
        self.connection.commit()
        return None

    # Fetches all triangles from the database and returns them as Triangle objects.
    def fetch_triangles(self):
        rows = self.cursor.execute('SELECT * FROM triangles').fetchall()
        return [Triangle.from_db_row(row) for row in rows]

    # Fetch a triangle by its name
    def fetch_triangle_by_name(self, name):
        row = self.cursor.execute(
            'SELECT * FROM triangles WHERE name = ?', (name,)).fetchone()
        if row:
            # Returns Triangle object and triangle_id from db
            return Triangle.from_db_row(row), row[0]
        return None

    # Fetch a triangle by its sorted points (as a string).
    def fetch_triangle_by_points(self, points):
        row = self.cursor.execute(
            'SELECT * FROM triangles WHERE points = ?', (points,)).fetchone()
        if row:
            return Triangle.from_db_row(row)
        return None

    # Update a triangle's information based on its ID.
    # Points are expected to be a list of tuples and will be sorted.
    def update_triangle(self, triangle_id, triangle: Triangle):
        updates = []
        values = []

        if triangle.name is not None:
            updates.append("name = ?")
            values.append(triangle.name)
        if triangle.points is not None:
            sorted_points = self._sort_points(triangle.points)
            existing_triangle = self.fetch_triangle_by_points(sorted_points)
            if existing_triangle and existing_triangle.id != triangle_id:
                err = "Cannot update: A triangle with the same points already exists."
                return err
            updates.append("points = ?")
            values.append(sorted_points)

        triangle_sides = calculation.triangle_points_to_sides(triangle.points)
        recalculated_triangle = calculation.calculate_triangle_data(
            triangle.name, triangle.points, triangle_sides)

        updates.append("perimeter = ?")
        values.append(recalculated_triangle.perimeter)

        updates.append("area = ?")
        values.append(recalculated_triangle.area)

        updates.append("type_based_on_sides = ?")
        values.append(recalculated_triangle.type_based_on_sides)

        updates.append("type_based_on_angles = ?")
        values.append(recalculated_triangle.type_based_on_angles)

        if updates:
            query = f"UPDATE triangles SET {', '.join(updates)} WHERE id = ?"
            values.append(triangle_id)
            self.cursor.execute(query, values)
            self.connection.commit()
        return None

    # Delete a triangle record based on its ID.
    def delete_triangle(self, triangle_id):
        self.cursor.execute(
            'DELETE FROM triangles WHERE id = ?', (triangle_id,))
        self.connection.commit()

    # Close the database connection.
    def close(self):
        self.connection.close()
