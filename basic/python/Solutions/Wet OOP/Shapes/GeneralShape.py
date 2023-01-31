import numpy as np
import cv2
import json
import abc

class GeneralShape(metaclass= abc.ABCMeta):
    @abc.abstractmethod
    def rotate_shape(self, rotation_angle: float):
        pass

    @abc.abstractmethod
    def translate_shape(self, translate_coordinates: (float, float)):
        pass

    @abc.abstractmethod
    def scale_shape(self, scale_coefficient: float):
        pass

    @abc.abstractmethod
    def draw_shape(self, image):
        pass
