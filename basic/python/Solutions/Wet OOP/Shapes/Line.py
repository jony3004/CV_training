import cv2
from Shapes.BasicShape import BasicShape


class Line(BasicShape):
    def __init__(self, coordinates, line_color, fill_color):
        super().__init__(coordinates, line_color, fill_color)

    def draw_shape(self, image):
        return cv2.line(image, (int(self._coordinates[0][0]), (int(self._coordinates[0][1]))),
                        (int(self._coordinates[1][0]), (int(self._coordinates[1][1]))),
                        self._line_color, 10)
