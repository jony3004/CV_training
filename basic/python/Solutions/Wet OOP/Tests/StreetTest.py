import unittest
from Extracting.ParserFromJSONFile import ParserFromJSONFile
class JSONParserTest(unittest.TestCase):
    def test_street_json(self):
        parser = ParserFromJSONFile()
        shape = parser.parse_path('../Street.json')
        self.assertAlmostEqual(100, shape.get_shapes()[0].get_shapes()[0].get_coordinates()[0][0], 4)
        self.assertAlmostEqual(208, shape.get_shapes()[0].get_shapes()[1].get_coordinates()[0][0], 4)
        self.assertAlmostEqual(-40, shape.get_shapes()[0].get_shapes()[1].get_coordinates()[0][1], 4)


if __name__ == '__main__':
    unittest.main()
