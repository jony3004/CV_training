import abc
from Shapes.GeneralShape import GeneralShape


class CompositeShape(GeneralShape, metaclass=abc.ABCMeta):
    def __init__(self, shapes_list: list[GeneralShape]):
        self._shapes_list = shapes_list

    def rotate_shape(self, rotation_angle: float):
        rotated_shapes = []
        for shape in self._shapes_list:
            rotated_shapes = shape.rotate_shape(rotation_angle)
        self._shapes_list = rotated_shapes

    def translate_shape(self, translate_coordinates: (float, float)):
        translated_shapes = []
        for shape in self._shapes_list:
            translated_shapes = shape.translate_shape(translate_coordinates)
        self._shapes_list = translated_shapes

    def scale_shape(self, scale_coefficient: float):
        scaled_shapes = []
        for shape in self._shapes_list:
            scaled_shapes = shape.scale_shape(scale_coefficient)
        self._shapes_list = scaled_shapes

    def add_shape(self, shape):
        self._shapes_list.append(shape)

    def draw_shape(self, image):
        for shape in self._shapes_list:
            shape.draw_shape(image)
