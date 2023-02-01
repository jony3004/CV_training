import cv2
from Shapes.BasicShape import BasicShape
class Point(BasicShape):
    def __init__(self, coordinates, line_color, fill_color):
        super().__init__(coordinates, line_color, fill_color)

    def draw_shape(self, image):
        return cv2.circle(image, (int(self._coordinates[0][0]), int(self._coordinates[0][1])),
                          1, self._line_color, -1)

