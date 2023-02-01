import matplotlib.pyplot as plt
import Shapes.GeneralShape


class ShapeDrawer:

    def __init__(self, image, shape: Shapes.GeneralShape):
        self._image = image
        self._shape = shape

    def draw_shape(self):
        self._image = self._shape.draw_shape(self._image)
        return self._image

    def save_image(self, image, JSON_path):
        plt.imshow(image)
        plt.title(JSON_path)
        plt.savefig("output.jpg")
        plt.show()

