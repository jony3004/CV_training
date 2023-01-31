import abc
import HelperFunctions
from Shapes.GeneralShape import GeneralShape


class BasicShape(GeneralShape, metaclass=abc.ABCMeta):
    def __init__(self, coordinates, line_color, fill_color):
        self._coordinates = coordinates
        self._line_color = HelperFunctions.hex_color_to_BGR(line_color)
        self._fill_color = HelperFunctions.hex_color_to_BGR(fill_color)

    def rotate_shape(self, rotation_angle: float):
        self._coordinates = HelperFunctions.rotate_coordinates_helper \
            (self._coordinates, rotation_angle)

    def translate_shape(self, translate_coordinates: (float, float)):
        translated_shape_points = []
        for point in self._coordinates:
            translated_shape_points.append((point[0] + translate_coordinates[0],
                                            point[1] + translate_coordinates[1]))
        self._coordinates = translated_shape_points

    def scale_shape(self, scale_coefficient: float):
        self._coordinates = HelperFunctions.scale_coordinates_helper(self._coordinates,
                                                                     scale_coefficient)

    def draw_shape(self, image):
        pass
