import json
import GeneralExerciseManager
import ShapeFactory
import Shapes.GeneralShape


class ParserFromJSONFile:
    def __init__(self):
        pass

    def parse_path(self, JSON_path):
        with open(JSON_path) as json_file:
            json_dict = json.load(json_file)
        shape = self.parse_shape(json_dict)
        shape = self.parse_extra_details(shape, json_dict)
        return shape

    def parse_shape(self, JSON_dict: dict):
        shape_factory = ShapeFactory.ShapeFactory()
        if "otherJsonPath" in JSON_dict:
            shape = self.parse_path(JSON_dict["otherJsonPath"])
        else:
            radius = -1
            if "radius" in JSON_dict:
                radius = JSON_dict["radius"]
            shape = shape_factory.create_shape(JSON_dict["shapeType"], JSON_dict["coords"],
                                               JSON_dict["lineColor"], JSON_dict["lineColor"],
                                               radius)

        if "containedShapes" in JSON_dict:
            for JSON_contained_dict in JSON_dict["containedShapes"]:
                shape.add_shape(self.parse_shape(JSON_contained_dict))
        return shape

    def parse_extra_details(self, shape: Shapes.GeneralShape, json_dict):
        if "translationX" in json_dict and "translationY" in json_dict:
            shape = shape.translate_shape((json_dict["translationX"],
                                           json_dict["translationY"]))

        if "rotationDeg" in json_dict:
            shape = shape.rotate_shape(json_dict["rotationDeg"])

        if "scale" in json_dict:
            shape = shape.scale_shape(json_dict["scale"])

        return shape
