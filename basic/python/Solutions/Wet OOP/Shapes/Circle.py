import cv2
from Shapes.BasicShape import BasicShape
class Circle(BasicShape):
    def __init__(self, coordinates, line_color, fill_color, radius):
        super().__init__(coordinates, line_color, fill_color)
        self._radius = radius

    def draw_shape(self, image):
        circle = cv2.circle(image, (int(self._coordinates[0][0]), (int(self._coordinates[0][1]))),
                          self._radius, self._fill_color, -1)
        return circle



