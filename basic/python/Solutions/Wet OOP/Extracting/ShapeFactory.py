import Shapes.CompositeShape
import Shapes.Point
import Shapes.Line
import Shapes.Circle
import Shapes.Rectangle
import Shapes.Triangle

class ShapeFactory:
    def __init__(self):
        pass

    def create_shape(self, shape_name, coordinates, line_color, fill_color, radius):
        coordinates = self.parse_coords(coordinates)
        if shape_name == "Point":
            return Shapes.Point.Point(coordinates, line_color, fill_color)
        if shape_name == "Line":
            return Shapes.Line.Line(coordinates, line_color, fill_color)
        if shape_name == "Circle":
            return Shapes.Circle.Circle(coordinates, line_color, fill_color, radius)
        if shape_name == "Rectangle":
            return Shapes.Rectangle.Rectangle(coordinates, line_color, fill_color)
        if shape_name == "Triangle":
            return Shapes.Triangle.Triangle(coordinates, line_color, fill_color)

        return Shapes.CompositeShape.CompositeShape([])

    def parse_coords(self, coordinates):
        coordinates_list = []
        for dictionary in coordinates:
            coordinates_list.append((dictionary["X"], dictionary["Y"]))
        return coordinates_list
