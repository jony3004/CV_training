import cv2
from Shapes.BasicShape import BasicShape
import numpy as np


class Rectangle(BasicShape):
    def __init__(self, coordinates, line_color, fill_color):
        super().__init__(coordinates, line_color, fill_color)

    def draw_shape(self, image):
        coordinates_array = np.array([[self._coordinates[0][0], self._coordinates[0][1]],
                                      [self._coordinates[1][0], self._coordinates[1][1]],
                                      [self._coordinates[2][0], self._coordinates[2][1]],
                                      [self._coordinates[3][0], self._coordinates[3][1]]], np.int32)

        coordinates_array = coordinates_array.reshape((-1, 1, 2))
        image = cv2.polylines(image, [coordinates_array], True, self._line_color, 1)
        return cv2.fillPoly(image, [coordinates_array], self._fill_color)
