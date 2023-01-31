import matplotlib.pyplot as plt
import Shapes.GeneralShape


class ShapeDrawer:

    def __init__(self, image, shape: Shapes.GeneralShape):
        self._image = image
        self._shape = shape

    def draw_shape(self):
        self._image = self._shape.draw_shape(self._image)

    def save_image(self) -> None:
        plt.imshow(self._image)
        plt.show()
        plt.savefig("output.jpg")
