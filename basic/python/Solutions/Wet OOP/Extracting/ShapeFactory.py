import Shapes.CompositeShape
import Shapes.Point
import Shapes.Line
import Shapes.Circle
import Shapes.Rectangle
import Shapes.Triangle


class ShapeFactory:
    def __init__(self):
        self._shape = None

    def create_composite_shape(self):
        return Shapes.CompositeShape.CompositeShape([])

    def create_shape(self, shape_name, coordinates, line_color, fill_color, radius):
        coordinates = self.parse_coords(coordinates)

        # CR: try to think of a way to avoid conditions. How can you use shape_name to access the right Shape class
        # with the same name?
        if shape_name == "Point":
            return Shapes.Point.Point(coordinates, line_color, fill_color)
        if shape_name == "Line":
            return Shapes.Line.Line(coordinates, line_color, fill_color)
        if shape_name == "Circle":
            return Shapes.Circle.Circle(coordinates, line_color, fill_color, radius)
        if shape_name == "Rectangle":
            return Shapes.Rectangle.Rectangle(coordinates, line_color, fill_color)

        return Shapes.Triangle.Triangle(coordinates, line_color, fill_color)


    def parse_coords(self, coordinates):
        # We change our coordinates to an easier form.
        coordinates_list = []
        for dictionary in coordinates:
            coordinates_list.append((int(dictionary["x"]), int(dictionary["y"])))
        return coordinates_list
