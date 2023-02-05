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
        shape_dict = {"Point": Shapes.Point.Point, "Line": Shapes.Line.Line,
                      "Circle": Shapes.Circle.Circle, "Rectangle": Shapes.Rectangle.Rectangle,
                      "Triangle": Shapes.Triangle.Triangle}

        if radius == -1:
            return shape_dict[shape_name](coordinates, line_color, fill_color)

        return shape_dict[shape_name](coordinates, line_color, fill_color, radius)


    def parse_coords(self, coordinates):
        # We change our coordinates to an easier form.
        coordinates_list = []
        for dictionary in coordinates:
            coordinates_list.append((int(dictionary["x"]), int(dictionary["y"])))
        return coordinates_list
