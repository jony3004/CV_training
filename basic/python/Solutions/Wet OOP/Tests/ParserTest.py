import unittest

from Extracting.ParserFromJSONFile import ParserFromJSONFile

class JSONParserTest(unittest.TestCase):
    def test_house_json(self):
        parser = ParserFromJSONFile()
        shape = parser.parse_path('../House.json')
        self.assertAlmostEqual(-60, shape._shapes_list[0]._coordinates[0][0], 4)
        self.assertAlmostEqual(40, shape._shapes_list[0]._coordinates[0][1], 4)
        self.assertAlmostEqual(-40, shape._shapes_list[0]._coordinates[1][0], 4)
        self.assertEqual(20, shape._shapes_list[1]._coordinates[1][1])
        self.assertEqual(-30, shape._shapes_list[2]._coordinates[2][0])
        self.assertEqual(0, shape._shapes_list[2]._coordinates[2][1])


if __name__ == '__main__':
    unittest.main()
