import cv2
import BasicShape


class Rectangle(BasicShape):
    def __init__(self, coordinates, line_color, fill_color):
        super.__init__(coordinates, line_color, fill_color)

    def draw_shape(self, image):
        return cv2.rectangle(image, self._coordinates[0],
                             self._coordinates[1], self._line_color, -1)
