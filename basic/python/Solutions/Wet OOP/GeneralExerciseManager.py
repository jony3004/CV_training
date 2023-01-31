import Extracting.ParserFromJSONFile as parser
import Extracting.ShapeDrawer as drawer
import Shapes.GeneralShape
import numpy as np


class GeneralExerciseManager:
    def __init__(self, JSON_path: str, image: np.ndarray):
        self._shape = None
        self._JSON_path = JSON_path
        self._image = image

    def shape_parse(self):
        file_parser = parser.ParserFromJSONFile()
        self._shape = file_parser.parse_path(self._JSON_path)

    def shape_to_image(self):
        image_drawer = drawer.ShapeDrawer(self._image, self._shape)
        drawn_image = image_drawer.draw_shape()
        image_drawer.save_image(drawn_image)


def main():
    exercise_manager = GeneralExerciseManager("", np.zeros(500, 500))
    exercise_manager.shape_parse()
    exercise_manager.shape_to_image()


if __name__ == "__main__":
    main()
