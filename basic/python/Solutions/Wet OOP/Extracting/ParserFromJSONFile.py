import json
import GeneralExerciseManager
from Extracting.ShapeFactory import ShapeFactory
import Shapes.GeneralShape
import Shapes.CompositeShape


class ParserFromJSONFile:
    def __init__(self):
        pass

    def parse_path(self, JSON_path):
        '''
                A method that is in charge of the parsing of the json file and the creation
                of according shapes.
                :param JSON_path: String, path to our json file.
                :return: shape: Shapes.GeneralShape
        '''
        with open(JSON_path) as json_file:
            json_dict = json.load(json_file)
        shape = self.parse_shape(json_dict)
        shape = self.parse_extra_details(shape, json_dict)
        if "containedShapes" in json_dict:
            shape = self.extra_details_helper_for_composite_shapes(json_dict, shape)
        return shape

    def extra_details_helper_for_composite_shapes(self, json_dict, shape):
        # Helper function for the case of a composite shape that handles the
        # possibility of a recursion of composite shapes.
        shape_list = shape.get_shapes()
        for i in range(len(shape_list)):
            if "containedShapes" in json_dict["containedShapes"][i]:
                # We call this function with recursion in case we have a
                # composite shape inside another composite shape.
                shape_list[i] = self.extra_details_helper_for_composite_shapes \
                    (json_dict["containedShapes"][i], shape_list[i])
            shape_list[i] = self.parse_extra_details(shape_list[i],
                                                     json_dict["containedShapes"][i])

        return shape

    def parse_shape(self, JSON_dict: dict):
        # We deal with both a json file that uses another JSON path, and one where
        # shapes are explicitly defined.

        # CR: shape_factory is not used in this function
        shape_factory = ShapeFactory()
        if "otherJsonPath" in JSON_dict:
            shape = self.parse_path(JSON_dict["otherJsonPath"])
            return shape
        else:
            if "containedShapes" in JSON_dict:
                return self.create_composite_shape(JSON_dict)
            else:
                return self.create_basic_shape(JSON_dict)

    def create_composite_shape(self, JSON_dict):
        # We deal with the creation of a composite shape, that includes the creation
        # of its contained shapes (basic or composite).

        # CR: If a composite shape with the same name and content appears twice in the JSON file, we parse it twice?
        # can you think of a way to avoid that?
        shape_factory = ShapeFactory()
        shape = shape_factory.create_composite_shape()
        for JSON_contained_dict in JSON_dict["containedShapes"]:
            shape.add_shape(self.parse_shape(JSON_contained_dict))

        return shape

    def create_basic_shape(self, JSON_dict):
        # Handles the creation of basic shapes.
        shape_factory = ShapeFactory()
        # A default radius for cases when a radius isn't defined (is only defined for circles).
        radius = -1
        if "radius" in JSON_dict:
            radius = JSON_dict["radius"]
        shape = shape_factory.create_shape(JSON_dict["shapeType"],
                                           JSON_dict["coords"], JSON_dict["lineColor"],
                                           JSON_dict["fillColor"], radius)

        return shape

    def parse_extra_details(self, shape: Shapes.GeneralShape, json_dict):
        '''
        A method that aims to rotate, translate and scale the newly created shape
        according to the json file description.
        :param shape: Shapes.GeneralShape
        :param json_dict: Dictionary
        :return: shape: Shapes.GeneralShape
        '''
        if "translationX" in json_dict and "translationY" in json_dict:
            shape = shape.translate_shape((json_dict["translationX"],
                                           json_dict["translationY"]))

        if "rotationDeg" in json_dict:
            shape = shape.rotate_shape(json_dict["rotationDeg"])

        if "scale" in json_dict:
            shape = shape.scale_shape(json_dict["scale"])

        return shape
