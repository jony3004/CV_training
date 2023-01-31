import cv2
import BasicShape


class Triangle(BasicShape):
    def __init__(self, coordinates, line_color, fill_color):
        super.__init__(coordinates, line_color, fill_color)

    def draw_shape(self, image):
        image = cv2.line(image, self._coordinates[0],
                         self._coordinates[1], self._line_color, -1)
        image = cv2.line(image, self._coordinates[0],
                         self._coordinates[2], self._line_color, -1)
        return cv2.line(image, self._coordinates[1],
                        self._coordinates[2], self._line_color, -1)
