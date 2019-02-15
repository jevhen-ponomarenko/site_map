import unittest
from parser import parse_file

class test_parse_file(unittest.TestCase):

    def test_parse_file_positive(self):
        parsed_file = parse_file('data/old_test.csv')
        # dictionary is not empty
        assert (len(list(parsed_file)) > 0)
