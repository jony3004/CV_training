import cv2
import BasicShape
class Circle(BasicShape):
    def __init__(self, coordinates, line_color, fill_color, radius):
        super.__init__(coordinates, line_color, fill_color)
        self._radius = radius

    def draw_shape(self, image):
        return cv2.circle(image, self._coordinates[0],
                          self._radius, self._line_color, -1)


